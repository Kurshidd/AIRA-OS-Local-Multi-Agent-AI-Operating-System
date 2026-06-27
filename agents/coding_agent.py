import re

from core.base_agent import BaseAgent
from tools.python_executor import execute_python


class CodingAgent(BaseAgent):

    def __init__(self, model):
        super().__init__("coding", model)

    def extract_code(self, text):
        """
        Extract Python code from Markdown code blocks.
        """

        pattern = r"```(?:python)?\s*(.*?)```"

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if match:
            return match.group(1).strip()

        return text.strip()

    def validate_code(self, code):
        """
        Basic safety validation.
        """

        blocked = [
            "os.remove",
            "os.rmdir",
            "shutil.rmtree",
            "subprocess.Popen",
            "subprocess.call",
            "eval(",
            "exec(",
        ]

        for item in blocked:
            if item in code:
                return False, f"Blocked operation detected: {item}"

        return True, ""

    def run(self, task, context=None):

        prompt = f"""
You are an expert Python developer.

Generate ONLY executable Python code.

Rules:

- Return ONLY raw Python code.
- Do NOT use markdown.
- Do NOT use ```python
- Do NOT explain anything.
- Do NOT use input().
- Use example values if input is needed.

Task:

{task}
"""

        raw_response = self.model.generate(
            [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        code = self.extract_code(raw_response)

        valid, reason = self.validate_code(code)

        if not valid:
            return f"Code execution blocked.\nReason: {reason}"

        output = execute_python(code)

        return f"""Generated Code:

{code}

Output:

{output}
"""