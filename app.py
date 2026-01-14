import streamlit as st
import pandas as pd
from src.data_loader import load_multiple_csv

st.set_page_config(
    page_title="Aadhaar Analyzer",
    layout="wide"
)

st.title("Aadhaar Enrolment Trend & Insight Analyzer")
st.caption("Evidence-based insights from enrolment, biometric & demographic data")

# ---------------- Sidebar ----------------
st.sidebar.header("Data Source")

choice = st.sidebar.radio(
    "Choose input type",
    [1, 2],
    format_func=lambda x: "Use default Aadhaar datasets" if x == 1 else "Upload CSV files"
)

# ---------------- Loader ----------------
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
            type="csv",
            accept_multiple_files=True
        )

        if uploaded_files:
            data = {}
            for file in uploaded_files:
                name = file.name.replace(".csv", "")
                data[name] = pd.read_csv(file)
            return data

        return None

# ---------------- Run ----------------
datasets = get_data_source(choice)

if datasets:
    st.success("Datasets loaded successfully ✅")

    for name, df in datasets.items():
        st.subheader(f"📂 {name.capitalize()} Dataset")
        st.write(f"Shape: {df.shape}")
        st.dataframe(df.head())

else:
    st.info("Please upload or select datasets to begin analysis.")
