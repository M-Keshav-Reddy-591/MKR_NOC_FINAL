import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Attendance")

employee_id = st.session_state.get(
    "employee_id"
)

# ===================================
# MARK ATTENDANCE
# ===================================

if st.button(
    "Mark Attendance",
    width="stretch"
):

    response = requests.post(

        f"{API}/api/v1/attendance/mark",

        json={
            "employee_id": employee_id
        }
    )

    if response.status_code == 200:

        st.success(
            response.json()["message"]
        )

    else:

        st.error(
            response.json()["detail"]
        )

st.divider()

# ===================================
# ATTENDANCE HISTORY
# ===================================

response = requests.get(
    f"{API}/api/v1/attendance/employee/{employee_id}"
)

if response.status_code == 200:

    data = response.json()

    if len(data) > 0:

        df = pd.DataFrame(data)

        st.subheader(
            "Attendance History"
        )

        st.dataframe(
            df,
            width="stretch"
        )

    else:

        st.info(
            "No attendance records found"
        )

else:

    st.error(
        "Unable to fetch attendance"
    )