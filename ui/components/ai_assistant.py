import os
import streamlit as st

from core.context.context_builder import ContextBuilder
from core.context.project_tree import (
    build_tree,
    get_cached_tree
)
from core.context.imports import extract_imports


TOOLS = [
    "🧠 Explain Code",
    "✨ Refactor",
    "⚡ Optimize",
    "🐞 Find Bugs",
    "🧪 Generate Tests",
    "📄 Generate Documentation",
    "🔄 Rewrite",
    "💬 Ask About File"
]


EXPLANATION_TOOLS = {
    "🧠 Explain Code",
    "🐞 Find Bugs",
    "💬 Ask About File"
}


def render():

    st.subheader("🤖 AI Assistant")

    selected_tool = st.selectbox(
        "Choose Action",
        TOOLS
    )

    prompt = st.text_area(
        "Additional Instructions",
        placeholder="Example: Optimize this function for speed..."
    )

    st.divider()

    if st.button(
        "🚀 Run AI",
        use_container_width=True
    ):

        selected_file = st.session_state.get(
            "selected_file"
        )

        if not selected_file:

            st.warning(
                "Please select a file first."
            )

            return

        try:

            # =====================================================
            # Current Source
            # =====================================================

            if st.session_state.get("editor_text"):

                code = st.session_state.editor_text

            else:

                with open(
                    selected_file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    code = f.read()

            # =====================================================
            # Context
            # =====================================================

            builder = ContextBuilder()

            context = builder.build(
                query=prompt
            )

            project_tree = get_cached_tree()

            if not project_tree:

                project_tree = build_tree()

            imports = extract_imports(code)

            relevance = context.get(
                "relevance",
                []
            )

            # =====================================================
            # Prompt
            # =====================================================

            full_prompt = f"""
You are AIRA OS.

You are an autonomous senior software engineer.

You always understand the entire project before modifying any file.

==================================================
PROJECT TREE
==================================================

{project_tree}

==================================================
CURRENT FILE
==================================================

{context.get("current_file")}

==================================================
OPEN TABS
==================================================

{context.get("open_tabs")}

==================================================
OPEN FILES
==================================================

{context.get("open_files")}

==================================================
SEMANTICALLY RELEVANT FILES
==================================================

{relevance}

==================================================
IMPORTS
==================================================

{imports}

==================================================
ACTIVE AGENT
==================================================

{context.get("active_agent")}

==================================================
METRICS
==================================================

{context.get("metrics")}

==================================================
RECENT REASONING
==================================================

{context.get("reasoning")}

==================================================
RECENT CHAT
==================================================

{context.get("chat")}

==================================================
EXECUTION TIMELINE
==================================================

{context.get("timeline")}

==================================================
TERMINAL
==================================================

{context.get("terminal")}

==================================================
CURRENT SOURCE
==================================================

{code}

==================================================
TASK
==================================================

Action:
{selected_tool}

Instructions:
{prompt}

==================================================
RULES
==================================================

1. Understand the whole project.

2. Use semantic search results.

3. Respect architecture.

4. Never break imports.

5. Preserve formatting.

6. Return ONLY the updated source code when modifying code.

7. Return Markdown only for explanation tasks.

8. Do not include unnecessary commentary.
"""

            # =====================================================
            # Run AI
            # =====================================================

            orchestrator = st.session_state["orchestrator"]

            with st.spinner(
                "🤖 AIRA is analyzing your project..."
            ):

                result = orchestrator.run(
                    full_prompt
                )

            ai_output = result["output"]

            # =====================================================
            # Save Runtime
            # =====================================================

            st.session_state.original_code = code
            st.session_state.generated_code = ai_output

            st.session_state.last_ai_task = {
                "tool": selected_tool,
                "file": selected_file,
                "prompt": prompt
            }

            st.success("✅ AI task completed.")

            # =====================================================
            # Context Summary
            # =====================================================

            with st.expander(
                "🧠 Semantic Project Memory"
            ):

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "Relevant Files",
                        len(relevance)
                    )

                    st.metric(
                        "Open Files",
                        len(
                            context.get(
                                "open_files",
                                []
                            )
                        )
                    )

                with c2:

                    st.metric(
                        "Open Tabs",
                        len(
                            context.get(
                                "open_tabs",
                                []
                            )
                        )
                    )

                    st.metric(
                        "Chat Messages",
                        len(
                            context.get(
                                "chat",
                                []
                            )
                        )
                    )

                st.divider()

                if relevance:

                    for item in relevance:

                        st.write(
                            f"⭐ **{item['score']}** — `{item['path']}`"
                        )

                else:

                    st.info(
                        "No semantic matches found."
                    )

            # =====================================================
            # Preview
            # =====================================================

            with st.expander(
                "👀 AI Output Preview",
                expanded=True
            ):

                if selected_tool in EXPLANATION_TOOLS:

                    st.markdown(ai_output)

                else:

                    extension = os.path.splitext(
                        selected_file
                    )[1].replace(".", "")

                    st.code(
                        ai_output,
                        language=extension or "text"
                    )

            # =====================================================
            # Download
            # =====================================================

            filename = (
                os.path.splitext(
                    os.path.basename(selected_file)
                )[0]
                + "_aira_output"
                + os.path.splitext(selected_file)[1]
            )

            st.download_button(
                "📥 Download Result",
                ai_output,
                file_name=filename,
                use_container_width=True
            )

        except Exception as e:

            st.error(f"❌ {str(e)}")