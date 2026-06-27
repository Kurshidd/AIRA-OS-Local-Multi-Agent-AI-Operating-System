import os

from core.context.project_cache import project_cache
from core.context.symbol_index import extract_symbols
from core.context.file_summary import summarize


IGNORE = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "venv",
    ".streamlit"
}


class WorkspaceIndexer:

    def build(self, root="."):

        project_cache.clear()

        indexed = 0

        for path, dirs, files in os.walk(root):

            dirs[:] = [
                d for d in dirs
                if d not in IGNORE
            ]

            for file in files:

                if not file.endswith(
                    (
                        ".py",
                        ".md",
                        ".json",
                        ".txt",
                        ".yaml",
                        ".yml"
                    )
                ):
                    continue

                full = os.path.join(
                    path,
                    file
                )

                try:

                    with open(
                        full,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        code = f.read()

                    project_cache.files[full] = code

                    project_cache.symbols[
                        full
                    ] = extract_symbols(code)

                    project_cache.summaries[
                        full
                    ] = summarize(
                        full,
                        code
                    )

                    indexed += 1

                except Exception:

                    pass

        return indexed


workspace_indexer = WorkspaceIndexer()