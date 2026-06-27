import os
import streamlit as st


IGNORE = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    ".streamlit",
    "venv",
    ".pytest_cache",
    ".mypy_cache",
    ".DS_Store"
}


FILE_ICONS = {
    ".py": "🐍",
    ".json": "🧩",
    ".md": "📝",
    ".txt": "📄",
    ".yaml": "⚙️",
    ".yml": "⚙️",
    ".toml": "⚙️",
    ".ini": "⚙️",
    ".csv": "📊",
    ".html": "🌐",
    ".css": "🎨",
    ".js": "🟨",
    ".ts": "🔷",
    ".jsx": "⚛️",
    ".tsx": "⚛️",
    ".sql": "🗄️",
    ".pdf": "📕",
    ".png": "🖼️",
    ".jpg": "🖼️",
    ".jpeg": "🖼️",
}


def file_icon(filename):

    ext = os.path.splitext(filename)[1].lower()

    return FILE_ICONS.get(ext, "📄")


def draw(path):

    try:

        items = sorted(
            os.listdir(path),
            key=lambda x: (
                not os.path.isdir(os.path.join(path, x)),
                x.lower()
            )
        )

    except Exception:
        return

    for item in items:

        if item in IGNORE:
            continue

        full = os.path.join(path, item)

        if os.path.isdir(full):

            with st.expander(f"📁 {item}"):

                draw(full)

        else:

            icon = file_icon(item)

            selected = (
                st.session_state.get("selected_file")
                == full
            )

            if selected:
                label = f"👉 {icon} {item}"
            else:
                label = f"{icon} {item}"

            if st.button(
                label,
                key=full,
                use_container_width=True
            ):

                st.session_state.selected_file = full


def render():

    st.subheader("📂 Explorer")

    st.caption(
        f"Project: {os.path.basename(os.getcwd())}"
    )

    draw(os.getcwd())