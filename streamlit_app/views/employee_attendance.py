import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"


def show_employee_attendance():

    st.title("Attendance")

    emp_id = st.session_state.get(
        "emp_id"
    )

    # MARK ATTENDANCE

    if st.button(
        "Mark Attendance",
        width="stretch"
    ):

        response = requests.post(

            f"{API}/api/v1/attendance/mark",

            json={

                "employee_id": emp_id

            }

        )

        if response.status_code == 200:

            st.success(
                response.json()["message"]
            )

        else:

            st.error(
                response.text
            )

    st.divider()

    # FETCH EMPLOYEE ATTENDANCE

    response = requests.get(
        f"{API}/api/v1/attendance/{emp_id}"
    )

    if response.status_code == 200:

        data = response.json()

        if len(data) > 0:

            df = pd.DataFrame(data)

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