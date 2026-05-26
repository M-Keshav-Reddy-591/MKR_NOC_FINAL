import streamlit as st
import pandas as pd

st.title("ATTENDANCE")

data = {
    "Date": [
        "2026-05-25",
        "2026-05-26"
    ],
    "Status": [
        "Present",
        "Absent"
    ]
}

df = pd.DataFrame(data)

st.dataframe(df)

if st.button("MARK ATTENDANCE"):

    st.success(
        "Attendance Marked"
    )