import os
import streamlit as st


IGNORE = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "venv",
    ".streamlit",
    ".pytest_cache",
    ".mypy_cache",
    ".DS_Store"
}


def build_tree(root="."):

    tree = []

    root = os.path.abspath(root)

    for path, dirs, files in os.walk(root):

        # ---------------------------------------
        # Ignore unwanted directories
        # ---------------------------------------

        dirs[:] = sorted(
            [
                d for d in dirs
                if d not in IGNORE
            ]
        )

        files = sorted(files)

        relative_path = os.path.relpath(path, root)

        level = 0 if relative_path == "." else relative_path.count(os.sep) + 1

        indent = "    " * level

        folder_name = (
            os.path.basename(root)
            if relative_path == "."
            else os.path.basename(path)
        )

        tree.append(f"{indent}📁 {folder_name}")

        for file in files:

            tree.append(
                f"{indent}    📄 {file}"
            )

    tree_text = "\n".join(tree)

    # ---------------------------------------
    # Cache Project Tree
    # ---------------------------------------

    try:

        st.session_state.project_tree = tree_text

    except Exception:

        pass

    return tree_text


def refresh_tree(root="."):

    """
    Force rebuild of the project tree.
    """

    return build_tree(root)


def get_cached_tree():

    """
    Return cached project tree if available.
    """

    return st.session_state.get(
        "project_tree",
        ""
    )