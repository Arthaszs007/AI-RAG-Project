from dataclasses import dataclass


@dataclass
class DocumentChunk:
    content: str
    source: str
    file_type: str
    extra: dict
