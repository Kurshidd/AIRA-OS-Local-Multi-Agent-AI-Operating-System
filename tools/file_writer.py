from pathlib import Path


def write_file(file_path, content):

    try:
        path = Path(file_path)

        path.write_text(content, encoding="utf-8")

        return f"Successfully wrote to {file_path}"

    except Exception as e:
        return str(e)