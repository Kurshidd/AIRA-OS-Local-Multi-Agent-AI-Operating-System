import streamlit as st


def render():

    st.subheader("🧠 Planner Reasoning")

    reasoning = st.session_state.get(
        "reasoning",
        []
    )

    if not reasoning:

        st.info("Waiting for planner...")

        return

    for step in reasoning[::-1]:

        st.write("•", step)