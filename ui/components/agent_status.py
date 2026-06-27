import streamlit as st

AGENTS = [
    "Planner",
    "Research",
    "Coding",
    "Memory",
    "Critic"
]


def render():

    st.subheader("🤖 Live Agents")

    active = st.session_state.get(
        "active_agent",
        "Idle"
    )

    for agent in AGENTS:

        if agent == active:

            st.success(f"🟢 {agent}")

        else:

            st.info(f"⚪ {agent}")

    st.divider()

    st.metric(
        "Current",
        active
    )