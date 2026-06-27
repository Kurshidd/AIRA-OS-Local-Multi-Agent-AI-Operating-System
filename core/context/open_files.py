from pathlib import Path
import os


class OpenFilesManager:

    def __init__(self):
        self.files = []

    # ----------------------------------------
    # Add File
    # ----------------------------------------

    def add(self, file_path):

        file_path = str(Path(file_path).resolve())

        if file_path not in self.files:
            self.files.append(file_path)

    # ----------------------------------------
    # Remove File
    # ----------------------------------------

    def remove(self, file_path):

        file_path = str(Path(file_path).resolve())

        if file_path in self.files:
            self.files.remove(file_path)

    # ----------------------------------------
    # List Files
    # ----------------------------------------

    def get_all(self):

        return list(self.files)

    # ----------------------------------------
    # Read Files
    # ----------------------------------------

    def read_all(self):

        output = []

        for file in self.files:

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                output.append({

                    "path": file,

                    "name": os.path.basename(file),

                    "extension": Path(file).suffix,

                    "directory": str(Path(file).parent),

                    "content": content,

                    "lines": len(content.splitlines()),

                    "characters": len(content),

                    "size_bytes": os.path.getsize(file)

                })

            except Exception:

                continue

        return output

    # ----------------------------------------
    # File Metadata
    # ----------------------------------------

    def get_metadata(self, file_path):

        file_path = str(Path(file_path).resolve())

        if not os.path.exists(file_path):
            return None

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

            return {

                "path": file_path,

                "name": os.path.basename(file_path),

                "extension": Path(file_path).suffix,

                "directory": str(Path(file_path).parent),

                "lines": len(content.splitlines()),

                "characters": len(content),

                "size_bytes": os.path.getsize(file_path)

            }

        except Exception:

            return None

    # ----------------------------------------
    # Check File
    # ----------------------------------------

    def exists(self, file_path):

        file_path = str(Path(file_path).resolve())

        return file_path in self.files

    # ----------------------------------------
    # Count
    # ----------------------------------------

    def count(self):

        return len(self.files)

    # ----------------------------------------
    # Clear
    # ----------------------------------------

    def clear(self):

        self.files.clear()


open_files = OpenFilesManager()