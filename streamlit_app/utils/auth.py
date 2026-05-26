import streamlit as st


def save_login(data):

    st.session_state["token"] = data["access_token"]

    st.session_state["role"] = data["role"]

    st.session_state["emp_id"] = data["emp_id"]

    st.session_state["emp_name"] = data["emp_name"]


def logout():

    st.session_state.clear()