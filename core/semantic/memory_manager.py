import os

from core.semantic.embedding_engine import EmbeddingEngine
from core.semantic.vector_store import vector_store
from core.context.imports import extract_imports


IGNORE = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "venv",
    ".streamlit",
    ".pytest_cache",
    ".mypy_cache"
}


class SemanticMemoryManager:

    def __init__(self):

        self.embedding = EmbeddingEngine()

    # --------------------------------------------------
    # Index Project
    # --------------------------------------------------

    def index_project(
        self,
        root="."
    ):

        vector_store.clear()

        indexed = 0

        for path, dirs, files in os.walk(root):

            dirs[:] = [

                d

                for d in dirs

                if d not in IGNORE

            ]

            for file in files:

                full_path = os.path.join(
                    path,
                    file
                )

                self.index_file(full_path)

                indexed += 1

        return indexed

    # --------------------------------------------------
    # Index One File
    # --------------------------------------------------

    def index_file(
        self,
        file_path
    ):

        try:

            with open(

                file_path,

                "r",

                encoding="utf-8"

            ) as f:

                code = f.read()

        except Exception:

            return False

        embedding = self.embedding.embed(code)

        metadata = {

            "imports": extract_imports(code),

            "lines": len(code.splitlines()),

            "characters": len(code)

        }

        vector_store.remove(file_path)

        vector_store.add(

            file_path=file_path,

            embedding=embedding,

            metadata=metadata

        )

        return True

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(
        self,
        file_path
    ):

        return self.index_file(file_path)

    # --------------------------------------------------
    # Remove
    # --------------------------------------------------

    def remove(
        self,
        file_path
    ):

        vector_store.remove(file_path)

    # --------------------------------------------------
    # Stats
    # --------------------------------------------------

    def stats(self):

        return {

            "indexed_files": vector_store.count()

        }


semantic_memory = SemanticMemoryManager()