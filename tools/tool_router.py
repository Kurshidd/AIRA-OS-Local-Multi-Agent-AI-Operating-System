import time

from core.logger import AgentLogger

from tools.file_reader import read_file
from tools.file_writer import write_file
from tools.folder_explorer import list_files
from tools.python_executor import execute_python
from tools.rag_tool import rag_search


def execute_plan(plan):

    start = time.time()

    retries = 0

    critic_status = "APPROVE"

    output = ""

    try:

        tool = plan.tool

        AgentLogger.info(f"Executing Tool : {tool}")

        if tool == "rag_search":

            output = rag_search(plan.user_input)

        elif tool == "python_executor":

            output = execute_python(plan.user_input)

        elif tool == "read_file":

            output = read_file(plan.user_input)

        elif tool == "write_file":

            output = write_file(plan.user_input)

        elif tool == "list_files":

            output = list_files(plan.user_input)

        else:

            output = "No tool execution required."

    except Exception as e:

        critic_status = "FAILED"

        retries += 1

        output = str(e)

        AgentLogger.error(output)

    execution_time = round(time.time() - start, 2)

    estimated_tokens = max(
        1,
        len(str(output).split()) * 1.3
    )

    return {

        "output": output,

        "metrics": {

            "planner": plan.agent,

            "tool": plan.tool,

            "time": execution_time,

            "tokens": int(estimated_tokens),

            "critic": critic_status,

            "retries": retries

        }

    }