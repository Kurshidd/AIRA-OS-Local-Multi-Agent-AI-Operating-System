from core.reflection import ReflectionEngine
import time


class ExecutionEngine:

    def __init__(self, registry, model):

        self.registry = registry
        self.reflector = ReflectionEngine(model)

    def execute(self, task):

        start = time.time()

        retries = 0

        agent = self.registry.get(task.agent)

        if agent is None:

            return {
                "output": f"Agent '{task.agent}' is not registered.",
                "metrics": {
                    "planner": task.agent,
                    "tool": task.tool,
                    "time": 0,
                    "tokens": 0,
                    "critic": "FAILED",
                    "retries": retries
                }
            }

        draft = agent.run(
            task.user_input,
            context=task
        )

        critic = self.registry.get("critic")

        critic_status = "SKIPPED"

        if critic:

            for _ in range(3):

                review = critic.run(
                    draft,
                    context=task
                )

                critic_status = review.get(
                    "status",
                    "APPROVE"
                )

                if critic_status == "APPROVE":
                    break

                retries += 1

                draft = self.reflector.improve(
                    task.user_input,
                    draft,
                    review.get("feedback", "")
                )

        elapsed = round(
            time.time() - start,
            2
        )

        tokens = int(len(str(draft).split()) * 1.3)

        return {

            "output": draft,

            "metrics": {

                "planner": task.agent,

                "tool": task.tool,

                "time": elapsed,

                "tokens": tokens,

                "critic": critic_status,

                "retries": retries

            }

        }