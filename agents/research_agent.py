from core.base_agent import BaseAgent
from tools.rag_tool import rag_search


class ResearchAgent(BaseAgent):

    def __init__(self, model):
        super().__init__("research", model)

    def run(self, task, context=None):

        knowledge = rag_search(task)

        prompt = f"""
You are a Research Agent.

Use the retrieved knowledge below to answer accurately.

Knowledge:
{knowledge}

User Question:
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