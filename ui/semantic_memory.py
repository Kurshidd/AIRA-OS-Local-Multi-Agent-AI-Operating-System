import streamlit as st

from core.semantic.memory_manager import semantic_memory


def render():

    st.subheader("🧠 Semantic Memory")

    if "semantic_initialized" not in st.session_state:

        with st.spinner("Indexing project..."):

            semantic_memory.index_project()

        st.session_state.semantic_initialized = True

    stats = semantic_memory.stats()

    st.metric(

        "Indexed Files",

        stats["indexed_files"]

    )

    if st.button(

        "🔄 Rebuild Semantic Index",

        use_container_width=True

    ):

        with st.spinner("Rebuilding..."):

            semantic_memory.index_project()

        st.success("Semantic memory rebuilt.")

        st.rerun()