import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .main {
            background-color: #f8fafc;
        }

        section[data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        section[data-testid="stSidebar"] * {
            color: white;
        }

        div.stButton > button {
            width: 100%;
            border-radius: 10px;
            height: 45px;
            background-color: #2563eb;
            color: white;
            font-weight: bold;
        }

        </style>
        """,
        unsafe_allow_html=True
    )