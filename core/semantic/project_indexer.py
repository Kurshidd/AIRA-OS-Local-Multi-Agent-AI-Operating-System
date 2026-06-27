import os
import ast
import json
from pathlib import Path
from datetime import datetime


IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    ".streamlit",
    "venv",
    ".pytest_cache",
    "node_modules",
    ".mypy_cache",
    "dist",
    "build"
}


SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".json",
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".html",
    ".css",
    ".sql"
}


class ProjectIndexer:

    def __init__(self, root="."):

        self.root = Path(root).resolve()

        self.index = []

    # --------------------------------------------------
    # Build Project Index
    # --------------------------------------------------

    def build(self):

        self.index = []

        for current_path, dirs, files in os.walk(self.root):

            dirs[:] = [
                d for d in dirs
                if d not in IGNORE_DIRS
            ]

            for file in files:

                path = Path(current_path) / file

                if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                    continue

                try:

                    self.index.append(
                        self.index_file(path)
                    )

                except Exception:
                    continue

        return self.index

    # --------------------------------------------------
    # Index One File
    # --------------------------------------------------

    def index_file(self, path):

        text = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        info = {

            "name": path.name,

            "path": str(path),

            "extension": path.suffix,

            "size": path.stat().st_size,

            "modified": datetime.fromtimestamp(
                path.stat().st_mtime
            ).isoformat(),

            "functions": [],

            "classes": [],

            "imports": [],

            "docstring": "",

            "comments": [],

            "text": text

        }

        if path.suffix == ".py":

            info.update(
                self.parse_python(text)
            )

        return info

    # --------------------------------------------------
    # Parse Python File
    # --------------------------------------------------

    def parse_python(self, source):

        result = {

            "functions": [],

            "classes": [],

            "imports": [],

            "docstring": "",

            "comments": []

        }

        try:

            tree = ast.parse(source)

        except Exception:

            return result

        result["docstring"] = ast.get_docstring(tree) or ""

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                result["functions"].append(
                    node.name
                )

            elif isinstance(node, ast.AsyncFunctionDef):

                result["functions"].append(
                    node.name
                )

            elif isinstance(node, ast.ClassDef):

                result["classes"].append(
                    node.name
                )

            elif isinstance(node, ast.Import):

                for alias in node.names:

                    result["imports"].append(
                        alias.name
                    )

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                result["imports"].append(
                    module
                )

        for line in source.splitlines():

            stripped = line.strip()

            if stripped.startswith("#"):

                result["comments"].append(
                    stripped
                )

        return result

    # --------------------------------------------------
    # Save Index
    # --------------------------------------------------

    def save(self, file="project_index.json"):

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.index,
                f,
                indent=4,
                ensure_ascii=False
            )

    # --------------------------------------------------
    # Load Index
    # --------------------------------------------------

    def load(self, file="project_index.json"):

        if not os.path.exists(file):

            return []

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            self.index = json.load(f)

        return self.index

    # --------------------------------------------------
    # Search by Filename
    # --------------------------------------------------

    def search(self, keyword):

        keyword = keyword.lower()

        return [

            item

            for item in self.index

            if keyword in item["name"].lower()

        ]

    # --------------------------------------------------
    # Return Index
    # --------------------------------------------------

    def get_index(self):

        return self.index


project_indexer = ProjectIndexer()