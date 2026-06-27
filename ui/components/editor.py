import os
import hashlib
import streamlit as st
from streamlit_monaco import st_monaco

from core.context.open_files import open_files


LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".json": "json",
    ".html": "html",
    ".css": "css",
    ".md": "markdown",
    ".txt": "text",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".sql": "sql",
    ".xml": "xml",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".cs": "csharp",
    ".go": "go",
    ".rs": "rust",
    ".php": "php"
}


def checksum(text: str):

    return hashlib.md5(
        text.encode("utf-8")
    ).hexdigest()


def render():

    st.subheader("📝 Code Editor")

    file = st.session_state.get("selected_file")

    if not file:

        st.info("Select a file from the Explorer.")
        return

    if not os.path.exists(file):

        st.error("Selected file does not exist.")
        return

    # --------------------------------------------------
    # Load File
    # --------------------------------------------------

    if (
        "editor_file" not in st.session_state
        or st.session_state.editor_file != file
    ):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        st.session_state.editor_text = text
        st.session_state.editor_file = file

        st.session_state.editor_checksum = checksum(text)
        st.session_state.file_dirty = False

        open_files.add(file)

        if "open_tabs" not in st.session_state:
            st.session_state.open_tabs = []

        if file not in st.session_state.open_tabs:
            st.session_state.open_tabs.append(file)

    extension = os.path.splitext(file)[1].lower()

    language = LANGUAGE_MAP.get(
        extension,
        "text"
    )

    # --------------------------------------------------
    # Monaco
    # --------------------------------------------------

    edited = st_monaco(
        value=st.session_state.editor_text,
        language=language,
        theme="vs-dark",
        height=650,
        key=file
    )

    st.session_state.editor_text = edited

    current_checksum = checksum(
        st.session_state.editor_text
    )

    st.session_state.file_dirty = (
        current_checksum
        != st.session_state.editor_checksum
    )

    # --------------------------------------------------
    # Toolbar
    # --------------------------------------------------

    save_col, reload_col, undo_col = st.columns(3)

    # ==========================
    # Save
    # ==========================

    with save_col:

        if st.button(
            "💾 Save",
            use_container_width=True
        ):

            try:

                with open(
                    file,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(
                        st.session_state.editor_text
                    )

                st.session_state.editor_checksum = checksum(
                    st.session_state.editor_text
                )

                st.session_state.file_dirty = False

                st.success("✅ File saved successfully.")

            except Exception as e:

                st.error(str(e))

    # ==========================
    # Reload
    # ==========================

    with reload_col:

        if st.button(
            "🔄 Reload",
            use_container_width=True
        ):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            st.session_state.editor_text = text

            st.session_state.editor_checksum = checksum(
                text
            )

            st.session_state.file_dirty = False

            st.rerun()

    # ==========================
    # Undo AI
    # ==========================

    with undo_col:

        if st.button(
            "↩ Undo AI",
            use_container_width=True
        ):

            if st.session_state.get("original_code"):

                st.session_state.editor_text = (
                    st.session_state.original_code
                )

                st.session_state.original_code = None
                st.session_state.generated_code = None

                st.session_state.file_dirty = True

                st.success("AI changes reverted.")

                st.rerun()

            else:

                st.info("No AI changes available.")

    # --------------------------------------------------
    # Status Bar
    # --------------------------------------------------

    left, center, right = st.columns(3)

    with left:

        if st.session_state.file_dirty:

            st.warning("● Unsaved Changes")

        else:

            st.success("● Saved")

    with center:

        st.caption(
            f"{len(st.session_state.editor_text.splitlines())} Lines"
        )

    with right:

        st.caption(
            f"{len(st.session_state.editor_text)} Characters"
        )

    st.caption(
        f"📄 {os.path.basename(file)}"
    )

    # --------------------------------------------------
    # Open Files
    # --------------------------------------------------

    with st.expander("📂 Open Files Manager"):

        files = open_files.get_all()

        if not files:

            st.info("No open files.")

        else:

            for i, path in enumerate(files, start=1):

                col1, col2 = st.columns([8, 1])

                with col1:

                    st.write(
                        f"{i}. {path}"
                    )

                with col2:

                    if st.button(
                        "❌",
                        key=f"close_{i}"
                    ):

                        open_files.remove(path)

                        if (
                            path
                            in st.session_state.open_tabs
                        ):

                            st.session_state.open_tabs.remove(path)

                        st.rerun()