import streamlit as st


def show_admin_dashboard():

    st.title("ADMIN DASHBOARD")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Employees",
            58
        )

    with col2:
        st.metric(
            "Present Today",
            44
        )

    with col3:
        st.metric(
            "Absent Today",
            14
        )

    st.divider()

    st.subheader("NOC Attendance Management System")

    st.success("System Running Successfully")