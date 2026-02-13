# Corrective RAG (CRAG) with LangGraph

A LangGraph implementation of the [CRAG paper](https://arxiv.org/pdf/2401.15884) — a self-correcting RAG pipeline that evaluates retrieved documents before using them for generation.

Instead of blindly trusting every retrieved document, CRAG adds a quality gate that scores each document and decides whether to use it, discard it, search the web, or do both.

## How It Works

1. **Retrieve** docs from FAISS vector store
2. **Evaluate** each doc with a lightweight LLM (Llama 3.2)
3. **Route** based on verdict:
   - **Correct** → Refine docs → Generate
   - **Incorrect** → Rewrite query → Web search → Refine → Generate
   - **Ambiguous** → Refine docs + Web search → Generate
4. **Refine** by decomposing docs into sentence-level strips and filtering out irrelevant ones
5. **Generate** the final answer using GPT-4o

## Tech Stack

- **LangGraph** — Pipeline orchestration with conditional routing
- **FAISS** — Vector store for document retrieval
- **OpenAI (GPT-4o)** — Generation and strip filtering
- **Ollama (Llama 3.2:3b)** — Lightweight local model for document evaluation
- **Tavily** — Web search fallback
- **LangChain** — Chains, prompts, and document handling

## Setup

### 1. Initialize and install dependencies

```bash
uv init .
uv add faiss-cpu huggingface ipykernel langchain langchain-community langchain-ollama langchain-openai langchain-tavily langchain-text-splitters pypdf python-dotenv
```

### 2. Set up environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

### 3. Make sure Ollama is running

```bash
ollama pull llama3.2:3b
```

### 4. Add your PDF

Place your PDF in the `./docs/` folder. The notebook uses `harrypotter.pdf` by default.

### 5. Run the notebook

Open the Jupyter notebook and run all cells top to bottom. The first run will take a while to load and embed the PDF — after that it's cached.

## References

- [CRAG Paper — Corrective Retrieval Augmented Generation](https://arxiv.org/pdf/2401.15884)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [CAMPUSX YOUTUBE CODE](https://www.youtube.com/watch?v=41XDn81nR5c)

