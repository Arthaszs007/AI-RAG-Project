"""
use for loading files to convert to string
support types: pdf, docx, text, md, excel, md
"""

import os
from typing import List, Dict
from pypdf import PdfReader
from docx import Document
import pandas as pd

from models.core_model import DocumentChunk


class DocumentParser:
    """
    PDF      → page
    Excel    → row
    DOCX     → paragraph
    TXT      → line
    MD       → line + section
    """

    def parse(self, file_path: str) -> List[Dict]:
        """
        invoke the func based on the file's type
        """
        ext = os.path.splitext(file_path)[-1].lower()

        if ext == ".pdf":
            return self._parser_pdf(file_path)
        elif ext == ".docx":
            return self._parser_docx(file_path)
        elif ext == ".xlsx":
            return self._parser_excel(file_path)
        elif ext == ".md":
            return self._parser_md(file_path)
        elif ext == ".txt":
            return self._parser_txt(file_path)
        else:
            return "your type of file is not support"

    def _parser_pdf(self, file_path: str) -> List[Dict]:
        """
        read .pdf file , convert to string in pages with metadata
        """
        reader = PdfReader(file_path)
        docs = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()

            if not text:
                continue

            docs.append(
                DocumentChunk(
                    content=text.strip(),
                    source=file_path,
                    file_type="pdf",
                    extra={
                        "page": i + 1,
                    },
                )
            )

        return docs

    def _parser_docx(self, file_path: str) -> List[Dict]:
        """
        read .docx file, convert to string in paragraphs with metadata
        """
        doc = Document(file_path)
        docs = []

        for i, para in enumerate(doc.paragraphs):
            text = para.text.strip()

            if not text:
                continue
            docs.append(
                DocumentChunk(
                    content=text,
                    file_type="docx",
                    source=file_path,
                    extra={"paragraph_id": i},
                )
            )

        return docs

    def _parser_excel(self, file_path: str) -> List[Dict]:
        """
        read .xslx file, convert to string in row with metadata
        """
        sheets = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")
        docs = []

        for sheet_name, df in sheets.items():
            df = df.fillna("")

            for i, row in df.iterrows():
                row_text = "|".join([str(x) for x in row.values])

                if not row_text.strip():
                    continue

                docs.append(
                    DocumentChunk(
                        content=row_text,
                        source=file_path,
                        file_type="xlsx",
                        extra={"row_id": i, "sheet": sheet_name},
                    )
                )

        return docs

    def _parser_txt(self, file_path: str) -> list[Dict]:
        """
        read .txt file, convert to string in line with metadata
        """
        docs = []
        with open(file_path, "r", encoding="utf-8") as f:

            for i, line in enumerate(f):

                text = line.strip()

                if not text:
                    continue

                docs.append(
                    DocumentChunk(
                        content=text,
                        source=file_path,
                        file_type="txt",
                        extra={"row_id": i},
                    )
                )
        return docs

    def _parser_md(self, file_path: str) -> List[Dict]:
        """
        read .md file, convert to string in line + section with metadata
        """
        docs = []
        current_header = ""

        with open(file_path, "r", encoding="utf-8") as f:

            for i, line in enumerate(f):
                text = line.strip()

                if not text:
                    continue

                if text.startswith("#"):
                    current_header = text.strip("# ").strip()
                    continue

                docs.append(
                    DocumentChunk(
                        content=text,
                        source=file_path,
                        file_type="md",
                        extra={"section": current_header, "row_id": i},
                    )
                )

        return docs
