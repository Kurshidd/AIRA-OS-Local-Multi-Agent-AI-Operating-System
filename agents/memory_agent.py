from core.base_agent import BaseAgent


class MemoryAgent(BaseAgent):

    def __init__(self, model, memory):
        super().__init__("memory", model)
        self.memory = memory

    def run(self, task, context=None):

        history = self.memory.get_recent_messages()

        conversation = ""

        for role, text in history:
            conversation += f"{role}: {text}\n"

        prompt = f"""
You are a Memory Agent.

Conversation:

{conversation}

User Request:

{task}
"""

        return self.model.generate(
            [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )