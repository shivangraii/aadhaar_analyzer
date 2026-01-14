import streamlit as st
import pandas as pd
from src.data_loader import load_multiple_csv  # adjust if needed

st.set_page_config(
    page_title="Aadhaar Analyzer",
    layout="wide"
)

# ---------- UI ----------
st.title("Aadhaar Enrolment Trend & Insight Analyzer")
st.caption("Data-driven insights for enrolment & update patterns")

st.sidebar.header("Data Source Selection")
choice = st.sidebar.radio(
    "Select data source",
    options=[1, 2],
    format_func=lambda x: "Use provided Aadhaar datasets" if x == 1 else "Upload custom CSV files"
)

# ---------- Logic ----------
def get_data_source(choice):
    if choice == 1:
        paths = [
            "data/saved/enrolment.csv",
            "data/saved/biometrics.csv",
            "data/saved/demographic.csv"
        ]
        return load_multiple_csv(paths)

    else:
        uploaded_files = st.sidebar.file_uploader(
            "Upload CSV files",
            type=["csv"],
            accept_multiple_files=True
        )

        if uploaded_files:
            dfs = [pd.read_csv(file) for file in uploaded_files]
            return pd.concat(dfs, ignore_index=True)

        return None

# ---------- Execution ----------
data = get_data_source(choice)

if data is not None:
    st.success("Data loaded successfully ✅")
    st.dataframe(data.head())
else:
    st.info("Please select or upload data to begin analysis.")
