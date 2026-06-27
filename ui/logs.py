import streamlit as st


def render_logs():

    st.subheader("📜 Logs")

    if "logs" not in st.session_state:
        st.session_state.logs = []

    if len(st.session_state.logs) == 0:
        st.info("No logs yet.")

    else:

        for log in st.session_state.logs[::-1]:
            st.code(log)