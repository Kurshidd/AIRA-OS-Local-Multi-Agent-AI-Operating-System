from typing import List
from sentence_transformers import SentenceTransformer


class EmbeddingEngine:
    """
    Production embedding engine utilizing sentence-transformers.
    Uses 'BAAI/bge-small-en-v1.5' for dense semantic vector extraction.
    """

    # BGE-small-en-v1.5 outputs vectors of size 384
    VECTOR_SIZE = 384

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    # --------------------------------------------------
    # Generate Embedding
    # --------------------------------------------------

    def embed(self, text: str) -> List[float]:
        """Generate a single normalized embedding vector."""
        if not text.strip():
            return [0.0] * self.VECTOR_SIZE

        # model.encode returns a numpy array; convert it to a standard Python list
        embeddings = self.model.encode(
            [text],
            normalize_embeddings=True,
            show_progress_bar=False
        )
        return embeddings[0].tolist()

    # --------------------------------------------------
    # Batch Embedding
    # --------------------------------------------------

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate a batch of normalized embedding vectors efficiently."""
        if not texts:
            return []

        # Clean/handle empty items inside batch
        processed_texts = [t if t.strip() else " " for t in texts]

        embeddings = self.model.encode(
            processed_texts,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        return embeddings.tolist()

    # --------------------------------------------------
    # Normalize Vector (Kept for interface backwards compatibility)
    # --------------------------------------------------

    def normalize(self, vector: List[float]) -> List[float]:
        """Normalizes a vector if not already normalized by the model pipeline."""
        magnitude = sum(
            value * value
            for value in vector
        ) ** 0.5

        if magnitude == 0:
            return vector

        return [
            value / magnitude
            for value in vector
        ]


# Export structural engine singleton instance for the indexer/vector store
embedding_engine = EmbeddingEngine()