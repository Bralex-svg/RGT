from fastapi import FastAPI
from chromadb import Client
from chromadb.config import Settings
from endpoints.endpoints import router as endpoint_router
from endpoints.models import Document
app = FastAPI()

settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory='chroma_data',
    chroma_api_impl="YOUR_CHROMA_API_IMPL_HERE"
)

chroma_url = "https://a0mqqykvni.execute-api.us-west-2.amazonaws.com/dev"

app.include_router(endpoint_router)

chroma_client = Client(chroma_url, settings=Settings)
































# from fastapi import FastAPI
# from chromadb import Client

# app = FastAPI()
# chroma_client = Client()
# collection = chroma_client.create_collection(name="my_collection")


# @app.post("/documents/")
# async def create_document(document: str, metadata: dict, doc_id: str):
#     collection.add(documents=[document], metadatas=[metadata], ids=[doc_id])
#     return {"message": "Document created successfully"}

# @app.get("/documents/{doc_id}")
# async def read_document(doc_id: str):
#     results = collection.query(query_texts=[doc_id], n_results=1)
#     return results

# @app.put("/documents/{doc_id}")
# async def update_document(doc_id: str, new_document: str, embeddings: list):
   
#     collection.update(doc_id, new_document, embeddings)
#     return {"message": "Document updated successfully"}


# @app.delete("/documents/{doc_id}")
# async def delete_document(doc_id: str):
#     collection.delete(doc_id)
#     return {"message": "Document deleted successfully"}
