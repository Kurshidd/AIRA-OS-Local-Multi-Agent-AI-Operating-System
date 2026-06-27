import streamlit as st


def render():

    st.subheader("📈 Timeline")

    timeline = st.session_state.get(
        "timeline",
        []
    )

    if not timeline:

        st.info("No execution yet.")

        return

    for item in timeline[::-1]:

        st.caption(item)