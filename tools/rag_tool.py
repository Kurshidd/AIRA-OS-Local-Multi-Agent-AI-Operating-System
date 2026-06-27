from rag.ingest import ingest_pdf
from rag.retrieval import search_documents


def rag_ingest(pdf_path):
    return ingest_pdf(pdf_path)


def rag_search(query):
    return search_documents(query)