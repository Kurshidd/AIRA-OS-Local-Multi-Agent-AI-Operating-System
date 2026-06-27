import streamlit as st

def load_css():
    st.markdown(
        """
        <style>

        /* Hide Streamlit default UI */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        /* Main app */
        .stApp {
            background-color: #0E1117;
            color: white;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #161B22;
            border-right: 1px solid #30363D;
        }

        /* Buttons */
        .stButton > button {
            width: 100%;
            border-radius: 10px;
            border: none;
            background-color: #2563EB;
            color: white;
            font-weight: bold;
            padding: 10px;
        }

        .stButton > button:hover {
            background-color: #1D4ED8;
            color: white;
        }

        /* Chat bubbles */
        .user-msg {
            background: #2563EB;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
            color: white;
        }

        .ai-msg {
            background: #1F2937;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
            color: white;
        }

        /* Status cards */
        .status-card {
            background-color: #1F2937;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 10px;
            border: 1px solid #374151;
        }

        h1,h2,h3,h4,h5,h6{
            color:white;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )