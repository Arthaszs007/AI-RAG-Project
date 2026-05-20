from back.core.parser import DocumentParser
from back.core.splitter import get_splitter
from back.core.doc_transfer import to_langchain_docs
from back.core.chroma import VectorBase

doc_parser = DocumentParser()
chroma = VectorBase()


def upload_file(files):

    splitter = get_splitter()

    chunks = []

    for file in files:

        chunks.extend(doc_parser.parse(file))

    docs = to_langchain_docs(chunks)

    split_docs = splitter.split_documents(docs)

    split_docs = [d for d in split_docs if d.page_content and d.page_content.strip()]

    # 必须加兜底
    if not split_docs:
        return

    chroma.save_to_base(split_docs)
