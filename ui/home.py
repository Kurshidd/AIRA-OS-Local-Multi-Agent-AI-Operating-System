import streamlit as st

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title="AIRA OS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# State
# ==========================================================

from ui.state import initialize_state

# ==========================================================
# Workspace Indexer
# ==========================================================

from core.context.workspace_indexer import workspace_indexer

# ==========================================================
# Left Panel
# ==========================================================

from ui.components.search import render as search
from ui.components.explorer import render as explorer
from ui.components.project_stats import render as project_stats

# ==========================================================
# Center Panel
# ==========================================================

from ui.chat import render_chat
from ui.components.editor import render as editor
from ui.components.preview import render as preview
from ui.components.file_tabs import render as file_tabs
from ui.components.ai_assistant import render as ai_assistant
from ui.components.diff_viewer import render as diff_viewer

# ==========================================================
# Right Panel
# ==========================================================

from ui.components.agent_status import render as render_agents
from ui.components.reasoning import render as render_reasoning
from ui.metrics import render_metrics

# ==========================================================
# Bottom Panel
# ==========================================================

from ui.terminal import render_terminal
from ui.logs import render_logs


def render_home():

    initialize_state()

    # ======================================================
    # Build Workspace Index (only once)
    # ======================================================

    if "workspace_indexed" not in st.session_state:

        count = workspace_indexer.build(".")

        st.session_state.workspace_indexed = True
        st.session_state.workspace_files = count

    # ======================================================
    # Header
    # ======================================================

    st.title("🤖 AIRA OS")

    st.caption(
        "Autonomous Multi-Agent AI Operating System"
    )

    # ======================================================
    # Workspace Toolbar
    # ======================================================

    toolbar1, toolbar2, toolbar3, toolbar4, toolbar5 = st.columns(
        [2, 1.5, 1.5, 1.5, 4]
    )

    # ------------------------------------------------------

    with toolbar1:

        if st.button(
            "🔄 Rebuild Index",
            use_container_width=True
        ):

            count = workspace_indexer.build(".")

            st.session_state.workspace_files = count

            st.success(
                f"Indexed {count} project files."
            )

    # ------------------------------------------------------

    with toolbar2:

        st.metric(
            "Workspace",
            st.session_state.get(
                "workspace_files",
                0
            )
        )

    # ------------------------------------------------------

    with toolbar3:

        st.metric(
            "Open Files",
            len(
                st.session_state.get(
                    "open_tabs",
                    []
                )
            )
        )

    # ------------------------------------------------------

    with toolbar4:

        st.metric(
            "Agent",
            st.session_state.get(
                "active_agent",
                "Idle"
            )
        )

    # ------------------------------------------------------

    with toolbar5:

        st.success(
            "🧠 Semantic Project Memory Ready"
        )

    st.divider()

    # ======================================================
    # Main Workspace
    # ======================================================

    left, center, right = st.columns(
        [1.25, 5.4, 1.45],
        gap="large"
    )

    # ======================================================
    # LEFT PANEL
    # ======================================================

    with left:

        search()

        st.divider()

        explorer()

        st.divider()

        project_stats()

    # ======================================================
    # CENTER PANEL
    # ======================================================

    with center:

        tab_chat, tab_workspace, tab_preview = st.tabs(
            [
                "💬 Chat",
                "📝 Workspace",
                "📄 Preview"
            ]
        )

        # --------------------------------------------------

        with tab_chat:

            render_chat()

        # --------------------------------------------------

        with tab_workspace:

            file_tabs()

            st.divider()

            editor_col, ai_col = st.columns(
                [4.3, 1.2],
                gap="large"
            )

            with editor_col:

                editor()

                st.divider()

                diff_viewer()

            with ai_col:

                ai_assistant()

        # --------------------------------------------------

        with tab_preview:

            preview()

    # ======================================================
    # RIGHT PANEL
    # ======================================================

    with right:

        render_agents()

        st.divider()

        render_reasoning()

        st.divider()

        render_metrics()

    # ======================================================
    # Bottom Workspace
    # ======================================================

    st.divider()

    terminal_col, logs_col = st.columns(
        [2.4, 1.6],
        gap="large"
    )

    with terminal_col:

        render_terminal()

    with logs_col:

        render_logs()

    # ======================================================
    # Footer
    # ======================================================

    st.divider()

    st.caption(
        f"AIRA OS v4.0.5 • Indexed {st.session_state.get('workspace_files', 0)} project files • Autonomous Multi-Agent Coding Workspace"
    )