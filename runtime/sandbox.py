import subprocess
import tempfile
import os


class Sandbox:

    @staticmethod
    def run_python(code):

        with tempfile.NamedTemporaryFile(

            delete=False,

            suffix=".py",

            mode="w",

            encoding="utf-8"

        ) as file:

            file.write(code)

            filename = file.name

        try:

            result = subprocess.run(

                ["python", filename],

                capture_output=True,

                text=True,

                timeout=10

            )

            return {

                "success": result.returncode == 0,

                "stdout": result.stdout,

                "stderr": result.stderr,

                "returncode": result.returncode

            }

        finally:

            os.remove(filename)