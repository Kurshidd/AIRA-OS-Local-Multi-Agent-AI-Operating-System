import streamlit as st


AGENTS = [

    "Planner",

    "Research",

    "Coding",

    "Memory",

    "Critic"

]


def render():

    st.subheader("🤖 Agents")

    active = st.session_state.active_agent

    for agent in AGENTS:

        if agent == active:

            st.success("🟢 " + agent)

        else:

            st.info("⚪ " + agent)