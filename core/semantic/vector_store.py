import math


class VectorStore:

    def __init__(self):

        self.documents = []

    # --------------------------------------------------
    # Clear Store
    # --------------------------------------------------

    def clear(self):

        self.documents = []

    # --------------------------------------------------
    # Add Document
    # --------------------------------------------------

    def add(

        self,

        file_path,

        embedding,

        metadata

    ):

        self.documents.append(

            {

                "path": file_path,

                "embedding": embedding,

                "metadata": metadata

            }

        )

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(self):

        return len(self.documents)

    # --------------------------------------------------
    # Get All
    # --------------------------------------------------

    def get_all(self):

        return self.documents

    # --------------------------------------------------
    # Cosine Similarity
    # --------------------------------------------------

    def cosine_similarity(

        self,

        vector1,

        vector2

    ):

        dot = sum(

            a * b

            for a, b in zip(vector1, vector2)

        )

        norm1 = math.sqrt(

            sum(

                a * a

                for a in vector1

            )

        )

        norm2 = math.sqrt(

            sum(

                b * b

                for b in vector2

            )

        )

        if norm1 == 0 or norm2 == 0:

            return 0.0

        return dot / (norm1 * norm2)

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(

        self,

        query_embedding,

        top_k=5

    ):

        scores = []

        for document in self.documents:

            score = self.cosine_similarity(

                query_embedding,

                document["embedding"]

            )

            scores.append(

                (

                    score,

                    document

                )

            )

        scores.sort(

            key=lambda x: x[0],

            reverse=True

        )

        results = []

        for score, document in scores[:top_k]:

            results.append(

                {

                    "score": round(score, 4),

                    "path": document["path"],

                    "metadata": document["metadata"]

                }

            )

        return results

    # --------------------------------------------------
    # Remove File
    # --------------------------------------------------

    def remove(

        self,

        file_path

    ):

        self.documents = [

            document

            for document in self.documents

            if document["path"] != file_path

        ]


vector_store = VectorStore()