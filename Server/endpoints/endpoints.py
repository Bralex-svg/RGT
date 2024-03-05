from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from database.get_db import get_db
from .models import Document
router = APIRouter()  

app = FastAPI()
class CreateDocument(APIRouter):
    @router.post("/documents/", response_model=Document)
    async def create_document(document: Document, db: Session = Depends(get_db)):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

class ReadDocument(APIRouter):
    @router.get("/documents/{doc_id}", response_model=Document)
    async def read_document(doc_id: str, db: Session = Depends(get_db)):
        results = db.query(Document).filter(Document.doc_id == doc_id).first()
        return results

class UpdateDocument(APIRouter):
    @router.put("/documents/{doc_id}", response_model=Document)
    async def update_document(doc_id: str, new_document: str, embeddings: list, db: Session = Depends(get_db)):
        document = db.query(Document).filter(Document.doc_id == doc_id).first()
        document.text = new_document
        document.embedding = embeddings
        db.commit()
        db.refresh(document)
        return document

class DeleteDocument(APIRouter):
    @router.delete("/documents/{doc_id}")
    async def delete_document(doc_id: str, db: Session = Depends(get_db)):
        document = db.query(Document).filter(Document.doc_id == doc_id).first()
        db.delete(document)
        db.commit()
        return {"message": "Document deleted successfully"}

app.include_router(router)
