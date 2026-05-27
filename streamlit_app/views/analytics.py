import streamlit as st
import pandas as pd
import numpy as np

def show_analytics():

    st.title("Analytics")

    data = pd.DataFrame({

        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May"
        ],

        "Attendance": [
            90,
            85,
            88,
            91,
            95
        ]
    })

    st.line_chart(
        data.set_index("Month")
    )