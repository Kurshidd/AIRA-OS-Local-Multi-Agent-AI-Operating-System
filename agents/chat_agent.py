from core.base_agent import BaseAgent


class ChatAgent(BaseAgent):

    def __init__(self, model):
        super().__init__("chat", model)

    def run(self, task, context=None):

        messages = [
            {
                "role": "user",
                "content": task
            }
        ]

        return self.model.generate(messages)