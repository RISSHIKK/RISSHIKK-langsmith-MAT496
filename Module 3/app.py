import os
import tempfile
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.sitemap import SitemapLoader
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings  # Using HuggingFace Embeddings
from langchain_groq import ChatGroq # Using Groq as the language model
from langsmith import traceable
from langsmith.client import convert_prompt_to_openai_format
from typing import List
import nest_asyncio

# Assuming a suitable Hugging Face embedding model
HF_EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
GROQ_MODEL_NAME = "openai/gpt-oss-120b" # Example Groq model name
MODEL_PROVIDER = "groq" # Updated provider
APP_VERSION = 1.0

RAG_SYSTEM_PROMPT = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the latest question in the conversation.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
"""

groq_chat = ChatGroq(temperature=0, model_name=GROQ_MODEL_NAME)

def get_vector_db_retriever():
    persist_path = os.path.join(tempfile.gettempdir(), "union.parquet")
    embd = HuggingFaceEmbeddings(model_name=HF_EMBEDDING_MODEL_NAME) # Changed to HuggingFace Embeddings

    # If vector store exists, then load it
    if os.path.exists(persist_path):
        vectorstore = SKLearnVectorStore(
            embedding=embd,
            persist_path=persist_path,
            serializer="parquet"
        )
        return vectorstore.as_retriever(lambda_mult=0)

    # Otherwise, index LangSmith documents and create new vector store
    ls_docs_sitemap_loader = SitemapLoader(web_path="https://docs.smith.langchain.com/sitemap.xml", continue_on_failure=True)
    ls_docs = ls_docs_sitemap_loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(ls_docs)

    vectorstore = SKLearnVectorStore.from_documents(
        documents=doc_splits,
        embedding=embd,
        persist_path=persist_path,
        serializer="parquet"
    )
    vectorstore.persist()
    return vectorstore.as_retriever(lambda_mult=0)

nest_asyncio.apply()
retriever = get_vector_db_retriever()

"""
retrieve_documents
- Returns documents fetched from a vectorstore based on the user's question
"""
@traceable(run_type="chain")
def retrieve_documents(question: str):
    return retriever.invoke(question)

"""
generate_response
- Calls `call_groq` to generate a model response after formatting inputs
"""
@traceable(run_type="chain")
def generate_response(question: str, documents):
    formatted_docs = "\n\n".join(doc.page_content for doc in documents)
    # TODO: Let's use our prompt pulled from Prompt Hub instead of manually formatting here!
    messages = [
        {
            "role": "system",
            "content": RAG_SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"Context: {formatted_docs} \n\n Question: {question}"
        }
    ]
    # formatted_prompt = prompt.invoke({"context":formatted_docs, "question": question})
    # messages = convert_prompt_to_openai_format(formatted_prompt)["messages"]
    return call_groq(messages) # Changed to call_groq

"""
call_groq
- Returns the chat completion output from Groq
"""
@traceable(
    run_type="llm",
    metadata={
        "ls_provider": MODEL_PROVIDER,
        "ls_model_name": GROQ_MODEL_NAME
    }
)
def call_groq(messages: List[dict]) -> str:
    # Groq Chat takes a list of messages as input
    return groq_chat.invoke(messages)


"""
langsmith_rag
- Calls `retrieve_documents` to fetch documents
- Calls `generate_response` to generate a response based on the fetched documents
- Returns the model response
"""
@traceable(run_type="chain")
def langsmith_rag(question: str):
    documents = retrieve_documents(question)
    response = generate_response(question, documents)
    # The response structure might be different for Groq,
    # you might need to adjust this line based on the actual response format
    return response.content