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
  
## Module 2:

**Vid 1 - Datasets:**  
    Learnt how to build and use datasets in Langsmith to evaluate AI systems offline, explained creating datasets through CSV import and manual entry, tagging versions for iteration, adding examples from real traces, splitting for specialized testing and exporting, building stable "golden" sets to measure improvements over time.  
    Changes made: Made changes in app.py (used Groq's "openai/gpt-oss-120b" model, used HuggingFaceEmbeddings instead of OpenAIEmbeddings), tested additional prompts to the model at the end  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/Source%20code/dataset_upload.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/dataset_upload_final.ipynb  

**Vid 2 - Evaluators:**  
    Learnt how to use evaluators in Langsmith to measure AI performance with metrics like accuracy and hallucination. It walks through creating custom evaluators, using LLMs as judges, handling RAG-specific evaluations and applying these evaluators to past runs for robust assessments.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model and tried my own example  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/Source%20code/evaluators.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/evaluators_final.ipynb  

**Vid 3 - Experiments:**  
    Learnt running experiments in Langsmith by combining datasets and evaluators, explained how to configure experiments via the UI or SDK, execute tests on full and partial datasets, tune models and parameters, enforce consistency, filter results and analyze outcomes within the experiments dashboard.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model and used HuggingFaceEmbeddings instead of OpenAIEmbeddings in the main code itself instead of app.py  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/Source%20code/experiments.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/Source%20code/experiments.ipynb  

**Vid 4 - Analyzing Experiment Results**  
    Learnt how to compare experiments in Langsmith through the UI, analyzing metrics like conciseness and similarity across runs. It shows how to filter experiments, inspect I/Os, review evaluator results and compare versions side by side to balance trade-offs such as latency v/s accuracy. Focus is on using experimentation to refine AI applications.  

**Vid 5 - Pairwise Experiments**  
    Learnt that pairwise evaluation lets you compare outputs from two experiments to see which performs better, especially helpful when a single result is difficult to score directly but easier to evaluate relative to another.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" and "llama-3.1-8b-instant" model   
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/Source%20code/pairwise_experiments.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/pairwise_experiments_final.ipynb  

**Vid 6 - Summary Evaluators**  
    Learnt about summary evaluators and how they provide overall metrics for an experiment(precision, recall, F1 score) rather than scoring an example, offering complete view of performance across the dataset.  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model and added a 'toxicity_label' to the F1 score section to ensure regardless of how model phrases its answer, evaluation only deals with two consistent classes - "Toxic" and "Not Toxic"  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/Source%20code/summary_evaluators.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%202/summary_evaluators_final.ipynb

## Module 3:

**Vid 1 - Playground:**  
    Learnt about how to use the playground feature in Langsmith, how to use the system and human messages to see outputs by playing with multiple LLM models, use other features used before like I/O schemas and tool callings, how to make own experiments and implement these features  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model in the Playground's "Messages" section, tried my own prompts and examples, added the screenshots of the AI responses observed with its corresponding parameters.  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%203/Source%20code/playground_experiments.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%203/playground_experiments_final.ipynb  

**Vid 2 - Prompts Hub:**  
    Learnt how to make custom structured prompts in the Prompt Hub, how to pull and upload a prompt from Langsmith, save/push prompt + model configuration as RunnableBinding object and create prompt commits  
    Changes made: Implemented using Groq's "openai/gpt-oss-120b" model in the code as well as in the Prompt commits, manually made hydrated prompts according to the Groq model, used the "french-rag-prompt" and "french-runnable-sequence" template and used custom hydrated prompts in French (generated by AI) to see model response  
    Source code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%203/Source%20code/prompt_hub.ipynb  
    Tweaked code: https://github.com/RISSHIKK/RISSHIKK-langsmith-MAT496/blob/main/Module%203/prompt_hub_final.ipynb  

**Vid 3 - Prompt Engineering Lifecycle:**
