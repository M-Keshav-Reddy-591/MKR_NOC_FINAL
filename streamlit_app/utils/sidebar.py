import streamlit as st


def admin_sidebar():

    with st.sidebar:

        st.title("ADMIN PANEL")

        menu = st.radio(

            "Navigation",

            [
                "Dashboard",
                "Employees",
                "Attendance",
                "Shift Management",
                "Analytics",
                "CSV Upload",
                "Reports",
                "Change Password"
            ]
        )

        if st.button("Logout"):

            st.session_state.clear()

            st.rerun()

    return menu