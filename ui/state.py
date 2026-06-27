import streamlit as st
from datetime import datetime

from runtime.event_bus import event_bus


class UIState:

    # ==========================================================
    # Initialize Session State
    # ==========================================================

    @staticmethod
    def initialize():

        defaults = {

            # -----------------------------
            # Chat
            # -----------------------------

            "messages": [],

            # -----------------------------
            # Logs
            # -----------------------------

            "logs": [],

            "timeline": [],

            "terminal": [],

            "reasoning": [],

            # -----------------------------
            # File System
            # -----------------------------

            "selected_file": None,

            "open_tabs": [],

            "project_tree": "",

            "context": {},

            "last_context_update": None,

            # -----------------------------
            # Monaco Editor
            # -----------------------------

            "editor_file": None,

            "editor_text": "",

            # -----------------------------
            # AI Diff Viewer
            # -----------------------------

            "original_code": None,

            "generated_code": None,

            # -----------------------------
            # Prompt Statistics
            # -----------------------------

            "prompt_size": 0,

            # -----------------------------
            # Runtime
            # -----------------------------

            "active_agent": "Idle",

            "metrics": {

                "planner": "-",

                "tool": "-",

                "tokens": 0,

                "time": 0,

                "critic": "-",

                "retries": 0,

                "context_files": 0

            },

            # -----------------------------
            # Event Bus
            # -----------------------------

            "events_initialized": False

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

        UIState.initialize_events()

    # ==========================================================
    # Event Registration
    # ==========================================================

    @staticmethod
    def initialize_events():

        if st.session_state.events_initialized:
            return

        event_bus.subscribe(
            "agent",
            UIState.set_agent
        )

        event_bus.subscribe(
            "reasoning",
            UIState.reasoning
        )

        event_bus.subscribe(
            "timeline",
            UIState.timeline
        )

        event_bus.subscribe(
            "log",
            UIState.log
        )

        event_bus.subscribe(
            "terminal",
            UIState.terminal
        )

        event_bus.subscribe(
            "metrics",
            UIState.metrics
        )

        st.session_state.events_initialized = True

    # ==========================================================
    # Logs
    # ==========================================================

    @staticmethod
    def log(text):

        st.session_state.logs.append(str(text))

    # ==========================================================
    # Terminal
    # ==========================================================

    @staticmethod
    def terminal(text):

        st.session_state.terminal.append(str(text))

    # ==========================================================
    # Planner Reasoning
    # ==========================================================

    @staticmethod
    def reasoning(text):

        st.session_state.reasoning.append(str(text))

    # ==========================================================
    # Timeline
    # ==========================================================

    @staticmethod
    def timeline(text):

        timestamp = datetime.now().strftime("%H:%M:%S")

        st.session_state.timeline.append(
            f"[{timestamp}] {text}"
        )

    # ==========================================================
    # Active Agent
    # ==========================================================

    @staticmethod
    def set_agent(agent):

        st.session_state.active_agent = str(agent)

    # ==========================================================
    # Metrics
    # ==========================================================

    @staticmethod
    def metrics(metrics):

        metrics = dict(metrics)

        context = st.session_state.get(
            "context",
            {}
        )

        metrics["context_files"] = len(
            context.get(
                "relevance",
                []
            )
        )

        metrics["open_files"] = len(
            context.get(
                "open_files",
                []
            )
        )

        metrics["open_tabs"] = len(
            context.get(
                "open_tabs",
                []
            )
        )

        metrics["prompt_size"] = st.session_state.get(
            "prompt_size",
            0
        )

        st.session_state.metrics = metrics

    # ==========================================================
    # Open Tabs
    # ==========================================================

    @staticmethod
    def add_tab(file_path):

        if (
            file_path
            and file_path not in st.session_state.open_tabs
        ):

            st.session_state.open_tabs.append(file_path)

    @staticmethod
    def remove_tab(file_path):

        if file_path in st.session_state.open_tabs:

            st.session_state.open_tabs.remove(file_path)

    # ==========================================================
    # Context
    # ==========================================================

    @staticmethod
    def set_context(context):

        st.session_state.context = context

    @staticmethod
    def get_context():

        return st.session_state.context

    # ==========================================================
    # Runtime Reset
    # ==========================================================

    @staticmethod
    def clear_runtime():

        st.session_state.logs = []

        st.session_state.timeline = []

        st.session_state.reasoning = []

        st.session_state.terminal = []

        st.session_state.active_agent = "Idle"

        st.session_state.original_code = None

        st.session_state.generated_code = None

        st.session_state.prompt_size = 0


# ==========================================================
# Compatibility Function
# ==========================================================

def initialize_state():

    UIState.initialize()