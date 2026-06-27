import re


def extract_code(text):

    pattern = r"```(?:python)?(.*?)```"

    match = re.search(
        pattern,
        text,
        re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return text.strip()