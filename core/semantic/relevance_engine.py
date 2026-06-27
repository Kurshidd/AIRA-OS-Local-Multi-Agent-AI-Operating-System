from core.semantic.embedding_engine import EmbeddingEngine
from core.semantic.vector_store import vector_store


class RelevanceEngine:

    def __init__(self):

        self.embedding = EmbeddingEngine()

    # --------------------------------------------------
    # Search Project
    # --------------------------------------------------

    def search(

        self,

        query,

        top_k=5

    ):

        query_embedding = self.embedding.embed(query)

        results = vector_store.search(

            query_embedding=query_embedding,

            top_k=top_k

        )

        return results

    # --------------------------------------------------
    # Search Current Context
    # --------------------------------------------------

    def search_context(

        self,

        context,

        top_k=5

    ):

        text = ""

        if context.get("current_code"):

            text += context["current_code"] + "\n"

        if context.get("reasoning"):

            text += "\n".join(

                context["reasoning"]

            )

        if context.get("chat"):

            for message in context["chat"]:

                text += "\n"

                text += str(message)

        return self.search(

            text,

            top_k

        )

    # --------------------------------------------------
    # Search Both Query + Context
    # --------------------------------------------------

    def search_everything(

        self,

        query,

        context,

        top_k=8

    ):

        combined = query

        if context.get("current_file"):

            combined += "\n"

            combined += context["current_file"]

        if context.get("current_code"):

            combined += "\n"

            combined += context["current_code"]

        if context.get("reasoning"):

            combined += "\n"

            combined += "\n".join(

                context["reasoning"]

            )

        return self.search(

            combined,

            top_k

        )


relevance_engine = RelevanceEngine()