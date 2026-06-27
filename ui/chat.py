import time
import streamlit as st

from ui.state import UIState
from runtime.event_bus import event_bus


# ==========================================================
# Initialization
# ==========================================================

def initialize_chat():

    UIState.initialize()

    if not st.session_state.messages:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": (
                    "👋 Hello! I'm **AIRA OS**.\n\n"
                    "How can I help you today?"
                )
            }
        )


# ==========================================================
# Streaming
# ==========================================================

def stream_response(text, placeholder):

    words = text.split()

    output = ""

    for word in words:

        output += word + " "

        placeholder.markdown(output + "▌")

        time.sleep(0.02)

    placeholder.markdown(output)

    return output


# ==========================================================
# Event Driven Agent Progress
# ==========================================================

def update_agent_progress(metrics):

    # Planner
    event_bus.publish("agent", "Planner")
    event_bus.publish("reasoning", "Understanding user request...")
    event_bus.publish("timeline", "Planner Started")

    # Research
    event_bus.publish("agent", "Research")
    event_bus.publish("reasoning", "Searching internal knowledge...")
    event_bus.publish("timeline", "Research Completed")

    # Coding
    event_bus.publish("agent", "Coding")
    event_bus.publish("reasoning", "Generating response...")
    event_bus.publish("timeline", "Coding Agent Executing")

    # Critic
    event_bus.publish("agent", "Critic")
    event_bus.publish("reasoning", "Reviewing response...")
    event_bus.publish("timeline", "Critic Approved")

    # Memory
    event_bus.publish("agent", "Memory")
    event_bus.publish("reasoning", "Updating memory...")
    event_bus.publish("timeline", "Conversation Stored")

    # Logs
    event_bus.publish(
        "log",
        f"Planner : {metrics['planner']}"
    )

    event_bus.publish(
        "log",
        f"Tool : {metrics['tool']}"
    )

    event_bus.publish(
        "log",
        f"Critic : {metrics['critic']}"
    )

    event_bus.publish(
        "log",
        f"Execution : {metrics['time']} sec"
    )

    # Metrics
    event_bus.publish(
        "metrics",
        metrics
    )

    # Idle
    event_bus.publish("agent", "Idle")


# ==========================================================
# Chat
# ==========================================================

def render_chat():

    initialize_chat()

    st.subheader("💬 Chat")

    # -------------------------------------------------------
    # Display Chat History
    # -------------------------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # -------------------------------------------------------
    # User Input
    # -------------------------------------------------------

    prompt = st.chat_input("Message AIRA...")

    if not prompt:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # -------------------------------------------------------
    # Assistant Response
    # -------------------------------------------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

        try:

            orchestrator = st.session_state["orchestrator"]

            memory = st.session_state["memory"]

            # Save User Message
            memory.save_message(
                "user",
                prompt
            )

            # Run Orchestrator
            result = orchestrator.run(prompt)

            response = result["output"]

            metrics = result["metrics"]

            # Streaming Response
            streamed = stream_response(
                response,
                placeholder
            )

            # Save Assistant Message
            memory.save_message(
                "assistant",
                streamed
            )

            # Update UI using Event Bus
            update_agent_progress(metrics)

            # Terminal Output
            event_bus.publish(
                "terminal",
                "> " + prompt
            )

            event_bus.publish(
                "terminal",
                streamed
            )

            # Save Chat History
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": streamed
                }
            )

            # Execution Metrics
            with st.expander("📊 Execution Details"):

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "Execution Time",
                        f"{metrics['time']} sec"
                    )

                    st.metric(
                        "Estimated Tokens",
                        metrics["tokens"]
                    )

                    st.metric(
                        "Retries",
                        metrics["retries"]
                    )

                with c2:

                    st.metric(
                        "Planner",
                        metrics["planner"]
                    )

                    st.metric(
                        "Tool",
                        metrics["tool"]
                    )

                    st.metric(
                        "Critic",
                        metrics["critic"]
                    )

        except Exception as e:

            event_bus.publish(
                "log",
                str(e)
            )

            event_bus.publish(
                "agent",
                "Idle"
            )

            placeholder.error(str(e))