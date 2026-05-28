import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

def show_reports():

    st.title("Attendance Reports")

    response = requests.get(
        f"{API}/api/v1/reports/all"
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
                "Download CSV",
                csv,
                "attendance_report.csv",
                "text/csv",
                width="stretch"
            )

        else:

            st.warning(
                "No attendance records found"
            )

    else:

        st.error(
            "Failed to load reports"
        )