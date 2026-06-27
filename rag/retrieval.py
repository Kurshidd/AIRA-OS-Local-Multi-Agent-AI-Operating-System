import chromadb

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_collection(
    name="documents"
)


def search_documents(query):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return "\n".join(
        results["documents"][0]
    )