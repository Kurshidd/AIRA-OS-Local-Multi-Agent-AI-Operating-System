from pathlib import Path


def read_file(file_path):

    path = Path(file_path)

    if not path.exists():
        return f"Error: {file_path} not found."

    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading file: {str(e)}"