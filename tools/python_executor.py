import subprocess
import tempfile
import os


def execute_python(code):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".py",
            mode="w",
            encoding="utf-8"
        ) as f:

            f.write(code)

            temp_file = f.name

        result = subprocess.run(
            ["python", temp_file],
            capture_output=True,
            text=True,
            timeout=10
        )

        os.remove(temp_file)

        return result.stdout or result.stderr

    except Exception as e:
        return str(e)