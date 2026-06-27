import streamlit as st


def render_metrics():

    st.subheader("📊 Performance")

    metrics = {}

    if "last_metrics" in st.session_state:
        metrics = st.session_state.last_metrics

    c1, c2 = st.columns(2)

    c1.metric(
        "Tokens",
        metrics.get("tokens", 0)
    )

    c2.metric(
        "Retries",
        metrics.get("retries", 0)
    )

    c1.metric(
        "Time",
        metrics.get("time", 0)
    )

    c2.metric(
        "Tool",
        metrics.get("tool", "-")
    )