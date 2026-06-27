class ReflectionEngine:

    def __init__(self, model):

        self.model = model

    def improve(self,
                user_request,
                draft,
                feedback):

        prompt = f"""
You are a Reflection Agent.

User Request:

{user_request}

Previous Answer:

{draft}

Critic Feedback:

{feedback}

Rewrite the answer.

Fix every issue.

Produce a better response.
"""

        return self.model.generate(
            [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )