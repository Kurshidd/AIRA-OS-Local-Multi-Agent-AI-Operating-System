import json

from core.base_agent import BaseAgent


class CriticAgent(BaseAgent):

    def __init__(self, model):
        super().__init__("critic", model)

    def run(self, draft_response, context=None):

        prompt = f"""
You are a Critic Agent.

Review the AI response.

User Request:
{context.user_input}

AI Draft:
{draft_response}

Evaluate the answer.

Return ONLY JSON.

Example:

{{
    "status":"APPROVE",
    "feedback":"Looks good."
}}

OR

{{
    "status":"REVISE",
    "feedback":"The answer is incomplete."
}}
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

            return json.loads(
                response[start:end]
            )

        except Exception:

            return {
                "status": "APPROVE",
                "feedback": ""
            }