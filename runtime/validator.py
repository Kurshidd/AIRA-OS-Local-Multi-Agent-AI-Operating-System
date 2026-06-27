from pathlib import Path


class ToolValidator:

    @staticmethod
    def validate_file(path):

        return Path(path).exists()

    @staticmethod
    def validate_python(code):

        blocked = [

            "eval(",
            "exec(",
            "os.remove",
            "os.rmdir",
            "shutil.rmtree",

            "subprocess.Popen",

            "__import__",

        ]

        for item in blocked:

            if item in code:

                return False

        return True