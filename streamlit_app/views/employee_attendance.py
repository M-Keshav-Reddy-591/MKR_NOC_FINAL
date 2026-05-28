import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

def show_employee_attendance():

    st.title("My Attendance")

    emp_id = st.session_state.emp_id

    response = requests.get(
        f"{API}/api/v1/reports/employee/{emp_id}"
    )

    if response.status_code == 200:

        data = response.json()

        if data:

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                width="stretch"
            )

            csv = df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                "Download My Attendance",
                csv,
                "my_attendance.csv",
                "text/csv",
                width="stretch"
            )

        else:

            st.warning(
                "No attendance records found"
            )

    else:

        st.error(
            "Failed to load attendance"
        )