import streamlit as st


def render():

    if "open_files" not in st.session_state:
        st.session_state.open_files = []

    selected = st.session_state.get("selected_file")

    if selected and selected not in st.session_state.open_files:
        st.session_state.open_files.append(selected)

    if not st.session_state.open_files:
        return

    cols = st.columns(len(st.session_state.open_files))

    for i, file in enumerate(st.session_state.open_files):

        name = file.split("\\")[-1].split("/")[-1]

        with cols[i]:

            if st.button(
                name,
                key=file,
                use_container_width=True
            ):

                st.session_state.selected_file = file