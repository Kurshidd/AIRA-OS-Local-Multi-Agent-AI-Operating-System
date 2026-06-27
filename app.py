import streamlit as st

from memory.memory import Memory
from models.local_model import LocalModel

from core.agent_registry import AgentRegistry
from core.execution_engine import ExecutionEngine
from core.orchestrator import Orchestrator

from agents.planner import Planner
from agents.chat_agent import ChatAgent
from agents.research_agent import ResearchAgent
from agents.coding_agent import CodingAgent
from agents.memory_agent import MemoryAgent
from agents.critic_agent import CriticAgent

from ui.styles import load_css
from ui.home import render_home


# ==================================================
# Streamlit Config
# ==================================================

st.set_page_config(
    page_title="AIRA OS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# ==================================================
# Initialize Backend (Only Once)
# ==================================================

@st.cache_resource
def initialize_backend():

    memory = Memory()

    model = LocalModel()

    planner = Planner(model)

    registry = AgentRegistry()

    execution_engine = ExecutionEngine(
        registry=registry,
        model=model
    )

    orchestrator = Orchestrator(
        planner=planner,
        execution_engine=execution_engine
    )

    registry.register(ChatAgent(model))
    registry.register(ResearchAgent(model))
    registry.register(CodingAgent(model))
    registry.register(MemoryAgent(model, memory))
    registry.register(CriticAgent(model))

    return orchestrator, memory


orchestrator, memory = initialize_backend()


# ==================================================
# Store in Session State
# ==================================================

st.session_state["orchestrator"] = orchestrator
st.session_state["memory"] = memory


# ==================================================
# Launch UI
# ==================================================

render_home()