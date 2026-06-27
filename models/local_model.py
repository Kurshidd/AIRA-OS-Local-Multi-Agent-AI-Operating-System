from ollama import chat


class LocalModel:

    def __init__(self, model_name="qwen3:8b"):
        self.model_name = model_name

    def generate(self, messages):
        response = chat(
            model=self.model_name,
            messages=messages
        )

        return response["message"]["content"]