from pathlib import Path


def list_files(folder="."):

    try:

        files = []

        for item in Path(folder).iterdir():
            files.append(item.name)

        return "\n".join(files)

    except Exception as e:
        return str(e)