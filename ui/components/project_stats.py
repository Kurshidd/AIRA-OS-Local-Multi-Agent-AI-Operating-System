import os
import streamlit as st


def render():

    total_files = 0
    total_dirs = 0

    for _, dirs, files in os.walk(os.getcwd()):

        total_dirs += len(dirs)
        total_files += len(files)

    st.subheader("📊 Project")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Files", total_files)

    with c2:
        st.metric("Folders", total_dirs)