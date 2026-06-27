import streamlit as st

from runtime.terminal_runner import TerminalRunner


def render_terminal():

    st.subheader("🖥 Terminal")

    if "terminal_history" not in st.session_state:
        st.session_state.terminal_history = []

    command = st.text_input(
        "Command",
        placeholder="python app.py"
    )

    col1, col2 = st.columns(2)

    with col1:

        run = st.button(
            "▶ Run",
            use_container_width=True
        )

    with col2:

        clear = st.button(
            "🗑 Clear",
            use_container_width=True
        )

    if clear:

        st.session_state.terminal_history = []

        st.rerun()

    if run and command:

        output = TerminalRunner.execute(command)

        st.session_state.terminal_history.append(
            f"> {command}"
        )

        st.session_state.terminal_history.append(output)

    st.divider()

    history = "\n\n".join(
        st.session_state.terminal_history
    )

    st.code(
        history if history else "Waiting for command..."
    )