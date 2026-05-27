import streamlit as st
import pandas as pd


def show_employees():

    st.title("EMPLOYEES")

    data = {

        "EMP ID": [
            "EMP001",
            "EMP002"
        ],

        "NAME": [
            "KESHAV",
            "PRAKASH"
        ],

        "DEPARTMENT": [
            "NOC",
            "NOC"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        width='stretch'
    )