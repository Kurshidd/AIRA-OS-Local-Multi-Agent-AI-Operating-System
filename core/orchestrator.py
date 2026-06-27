import time


class Orchestrator:

    def __init__(self, planner, execution_engine):

        self.planner = planner
        self.execution_engine = execution_engine

    def run(self, user_input):

        total_start = time.time()

        plan = self.planner.run(user_input)

        result = self.execution_engine.execute(plan)

        total_time = time.time() - total_start

        result["runtime"] = round(total_time, 2)

        return result