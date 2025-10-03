# RISSHIKK-langsmith-MAT496

## Module 1:

**Vid 1 - Tracing Basics:**  
  Learnt that the @traceable function in langsmith makes it easier to track function calls by automatically creating a structured "run tree." This feature lets you monitor performance, add metadata for filtering, and analyze execution flows more effectively.  
  Changes made: Implemented using Groq's "openai/gpt-oss-120b" model, used HuggingFaceEmbeddings and FAISS for Embeddings and Vector db, tested additional prompts to the model at the end  
  Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/Source%20Codes/tracing_basics.ipynb  
  Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/tracing_basics_final.ipynb  

**Vid 2 - Types of Runs:**  
    Learnt how to set up observability for Langchain agents, covering LLM, retriever, and tool runs. It shows how to trace, log, visualize runs in langsmith, manage streaming outputs, format data, add tracking metadata, and use the langsmith playground for debugging and workflow optimization.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model and tested my own examples at the end  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/Source%20Codes/types_of_runs.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/types_of_runs_final.ipynb   
    
**Vid 3 - Alternative Tracing Methods:**  
    Learnt various ways to add tracing in LangChain applications like using the @traceable decorator for automatic run tree generation and also other tracing approaches such as environment variables, context managers, and wrapping OpenAI SDK calls for improved monitoring and debugging in LangSmith.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model, modified utils.py (to use HuggingFaceEmbeddings) to adapt to the usage of main implementation, tested my own examples at the end  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/Source%20Codes/alternative_tracing_methods.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/alternative_tracing_methods_final.ipynb  

**Vid 4 - Conversational Threads:**  
    Learnt conversational threads in Langchain, explains how multiple chat interactions can be grouped together using thread IDs. It demonstrates how Langsmith can display and debug entire conversations as threads with complete trace details and performance metrics.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model, modified utils.py (to use HuggingFaceEmbeddings) to adapt to the usage of main implementation, tested additional prompts to the model at the end  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/Source%20Codes/conversational_threads.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%201/conversational_threads_final.ipynb  
