import os
import streamlit as st


def render():

    st.subheader("🔍 Search")

    query = st.text_input(
        "Find file"
    )

    if not query:
        return

    for root, _, files in os.walk(os.getcwd()):

        for file in files:

            if query.lower() in file.lower():

                full = os.path.join(root, file)

                if st.button(
                    file,
                    key=full
                ):
                    st.session_state.selected_file = full