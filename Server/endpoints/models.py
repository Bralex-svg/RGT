from pydantic import BaseModel
from typing import List

class Document(BaseModel):
    document: str
    metadata: dict
    doc_id: str

class UpdateDocument(BaseModel):
    new_document: str
    embeddings: List[float]
