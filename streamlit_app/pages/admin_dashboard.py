import streamlit as st

st.title("ADMIN DASHBOARD")

col1, col2, col3 = st.columns(3)

col1.metric("Employees", 58)

col2.metric("Present", 41)

col3.metric("Absent", 17)

st.success("NOC Monitoring Active")