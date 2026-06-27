import streamlit as st
import os


def render():

    st.subheader("📄 Preview")

    file = st.session_state.selected_file

    if not file:

        st.info("Select a file.")

        return

    if not os.path.exists(file):

        st.error("File not found.")

        return

    try:

        with open(file, "r", encoding="utf-8") as f:

            text = f.read()

        st.code(text)

    except Exception as e:

        st.error(str(e))