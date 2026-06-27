import os
import fitz
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(name="documents")

def ingest_pdf(pdf_path):
    # Check if the file doesn't exist at the given path, but exists inside the 'data' directory
    if not os.path.exists(pdf_path):
        fallback_path = os.path.join("data", pdf_path)
        if os.path.exists(fallback_path):
            pdf_path = fallback_path

    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    chunks = []
    chunk_size = 500

    for i in range(0, len(full_text), chunk_size):
        chunks.append(full_text[i:i + chunk_size])

    for idx, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[f"{pdf_path}_{idx}"],
            embeddings=[embedding],
            documents=[chunk]
        )

    return f"{len(chunks)} chunks added from {pdf_path}."