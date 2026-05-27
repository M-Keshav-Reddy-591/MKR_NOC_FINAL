import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000/api/v1"

def show_attendance():

    st.title("Attendance")

    employee = st.session_state.employee

    if st.button("Mark Attendance"):

        payload = {

            "employee_id": employee["id"]
        }

        try:

            response = requests.post(

                f"{API}/attendance/mark",

                json=payload
            )

            if response.status_code == 200:

                st.success(
                    "Attendance Marked"
                )

            else:

                st.error(
                    response.text
                )

        except Exception as e:

            st.error(str(e))

    st.divider()

    try:

        response = requests.get(
            f"{API}/attendance"
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width="stretch"
        )

    except Exception as e:

        st.error(str(e))



