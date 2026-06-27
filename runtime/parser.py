import json
import re


class OutputParser:

    @staticmethod
    def extract_json(text):

        try:

            start = text.find("{")
            end = text.rfind("}") + 1

            return json.loads(
                text[start:end]
            )

        except:

            return None

    @staticmethod
    def extract_code(text):

        pattern = r"```(?:python)?\s*(.*?)```"

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if match:
            return match.group(1).strip()

        return text.strip()