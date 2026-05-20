"""
convert file type to Document in langchain
"""

from typing import List
from langchain_core.documents import Document
from back.models.core_model import DocumentChunk


def to_langchain_docs(chunks: List[DocumentChunk]) -> List[Document]:
    """
    type convert to Document in langchain
    """
    return [
        Document(
            page_content=d.content,
            metadata={"source": d.source, "file_type": d.file_type, **d.extra},
        )
        for d in chunks
    ]
