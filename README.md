# LightRAG demo

LightRAG is a lightweight RAG library that allows you to build a knowledge graph and perform semantic search over it.

Based on the [LightRAG](https://github.com/HKUDS/LightRAG) library.

# How to run

1) Install dependencies:

```bash
pip install -r requirements.txt
```

2) Set the following environment variables:

- `OPENAI_API_KEY`
- `OPENAI_API_BASE` (default: https://api.openai.com/v1)
- `LLM_MODEL` (default: gpt-4o-mini)
- `EMBEDDING_MODEL` (default: text-embedding-3-large)

Then just run the `main.py` file.
It will initialize the RAG and create a knowledge graph from the `data/szymkiewicz.txt` file, as well as embeddings.
You can modify query, type of search, etc.
