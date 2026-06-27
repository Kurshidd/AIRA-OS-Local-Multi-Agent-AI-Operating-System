import json

from core.base_agent import BaseAgent
from core.task import Task


class Planner(BaseAgent):

    def __init__(self, model):
        super().__init__("planner", model)

    def run(self, task, context=None):

        prompt = f"""
You are an AI Planning Agent.

Available agents:

chat
research
coding
memory

Available tools:

rag_search
python_executor
none

Return ONLY JSON.

Example:

{{
"agent":"research",
"tool":"rag_search",
"confidence":0.95,
"reason":"Question requires document retrieval."
}}

User:

{task}
"""

        response = self.model.generate(
            [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        try:

            start = response.find("{")
            end = response.rfind("}") + 1

            plan = json.loads(response[start:end])

            return Task(
                user_input=task,
                agent=plan.get("agent", "chat"),
                tool=plan.get("tool", "none"),
                confidence=plan.get("confidence", 1.0),
                reason=plan.get("reason", "")
            )

        except Exception:

            return Task(user_input=task)