"""
create a chroma
"""

from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import back.config as config
from back.models import core_model

from dotenv import load_dotenv

load_dotenv()


class VectorBase:
    def __init__(self):
        self.chroma = Chroma(
            collection_name=config.COLLECTION_NAME,
            embedding_function=(DashScopeEmbeddings(model=config.EMBEDDING_MODEL_NAME)),
            persist_directory=config.PERSIST_DIRECTORY,
        )

    def save_to_base(self, chunks: core_model.DocumentChunk):
        chunks = [c for c in chunks if c.page_content and c.page_content.strip()]

        if not chunks:
            print("empty docs, skip embedding")
            return

        self.chroma.add_documents(chunks)

    def get_retriever(self):
        return self.chroma.as_retriever(search_kwarge={"k": config.SIMILAR_SEARCH_KWG})
