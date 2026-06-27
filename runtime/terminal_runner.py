import subprocess
import os


class TerminalRunner:

    @staticmethod
    def execute(command: str):

        command = command.strip()

        if not command:
            return ""

        try:

            result = subprocess.run(
                command,
                shell=True,
                cwd=os.getcwd(),
                capture_output=True,
                text=True
            )

            output = result.stdout

            if result.stderr:
                output += "\n" + result.stderr

            return output.strip()

        except Exception as e:
            return str(e)