import streamlit as st


def show_analytics():

    st.title("ANALYTICS")

    st.line_chart({

        "Attendance": [
            85,
            88,
            91,
            87,
            93
        ]
    })