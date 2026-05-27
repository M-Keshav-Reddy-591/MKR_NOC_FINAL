import streamlit as st


def show_change_password():

    st.title("CHANGE PASSWORD")

    old_password = st.text_input(
        "Old Password",
        type="password"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    if st.button("Update Password"):

        st.success(
            "Password Updated"
        )