"""
create a split tool
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

import back.config as config


def get_splitter():
    """
    create a splitter tool and return it
    options coming from config file
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=config.SEPARATOR,
        length_function=len,
    )
