import streamlit as st
import pandas as pd

st.title("MONTHLY ANALYTICS")

data = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr"
    ],
    "Attendance": [
        90,
        84,
        95,
        88
    ]
})

st.line_chart(
    data.set_index("Month")
)