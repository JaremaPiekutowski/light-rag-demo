import os
import asyncio

import PyPDF2

from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger

setup_logger("lightrag", level="INFO")

load_dotenv()

if not os.path.exists("rag"):
    os.makedirs("rag")

async def initialize_rag():
    rag = LightRAG(
        working_dir="rag",
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    return rag

def main():
    print(os.getenv("OPENAI_API_BASE"))

    # Initialize RAG instance
    rag = asyncio.run(initialize_rag())

    with open("data/szymkiewicz.txt", "r") as file:
        text = file.read()

    rag.insert(text)

    # Mix mode Integrates knowledge graph and vector retrieval.
    # # Other modes: naive, local, global, hybrid
    mode="mix"

    response = rag.query(
        "Kim jest Kryzys, przyjaciel Jacka Szymkiewicza?",
        param=QueryParam(mode=mode)
    )

    print(response)


if __name__ == "__main__":
    main()
