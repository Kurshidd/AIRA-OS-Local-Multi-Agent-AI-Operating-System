import streamlit as st

from core.context.open_files import open_files
from core.context.project_cache import project_cache


class ContextBuilder:

    def __init__(self):
        pass

    def build(self):

        context = {}

        # ==================================================
        # Current File
        # ==================================================

        context["current_file"] = st.session_state.get(
            "selected_file"
        )

        # ==================================================
        # Current Editor
        # ==================================================

        context["current_code"] = st.session_state.get(
            "editor_text",
            ""
        )

        # ==================================================
        # Open Tabs
        # ==================================================

        context["open_tabs"] = st.session_state.get(
            "open_tabs",
            []
        )

        # ==================================================
        # Open Files
        # ==================================================

        context["open_files"] = open_files.get_all()

        context["open_file_contents"] = open_files.read_all()

        # ==================================================
        # Workspace Index
        # ==================================================

        context["workspace_files"] = list(
            project_cache.files.keys()
        )

        context["workspace_summaries"] = list(
            project_cache.summaries.values()
        )

        context["workspace_symbols"] = (
            project_cache.symbols
        )

        # ==================================================
        # Relevance Engine
        # ==================================================

        context["relevance"] = []

        # ==================================================
        # Project Tree
        # ==================================================

        context["project_tree"] = st.session_state.get(
            "project_tree",
            ""
        )

        # ==================================================
        # Conversation
        # ==================================================

        context["chat"] = st.session_state.get(
            "messages",
            []
        )[-10:]

        # ==================================================
        # Planner
        # ==================================================

        context["reasoning"] = st.session_state.get(
            "reasoning",
            []
        )[-20:]

        # ==================================================
        # Runtime
        # ==================================================

        context["metrics"] = st.session_state.get(
            "metrics",
            {}
        )

        context["active_agent"] = st.session_state.get(
            "active_agent",
            "Idle"
        )

        context["timeline"] = st.session_state.get(
            "timeline",
            []
        )[-20:]

        context["logs"] = st.session_state.get(
            "logs",
            []
        )[-30:]

        context["terminal"] = st.session_state.get(
            "terminal",
            []
        )[-20:]

        # ==================================================
        # Store
        # ==================================================

        st.session_state.context = context

        return context