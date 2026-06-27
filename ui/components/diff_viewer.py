import difflib
import streamlit as st


def render():

    original = st.session_state.get("original_code")
    modified = st.session_state.get("generated_code")

    if not original or not modified:
        return

    st.subheader("📄 AI Diff Preview")

    diff = difflib.unified_diff(
        original.splitlines(),
        modified.splitlines(),
        fromfile="Original",
        tofile="AI",
        lineterm=""
    )

    st.code("\n".join(diff), language="diff")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "✅ Apply Changes",
            use_container_width=True
        ):

            st.session_state.editor_text = modified

            st.session_state.original_code = None
            st.session_state.generated_code = None

            st.success("Changes applied.")

    with col2:

        if st.button(
            "❌ Reject",
            use_container_width=True
        ):

            st.session_state.original_code = None
            st.session_state.generated_code = None

            st.info("Changes discarded.")