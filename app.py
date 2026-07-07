import streamlit as st
from src.data_loader import load_data
from src.clean_data import clean_data
from src.analysis import (
    prepare_data,
    get_unique_countries,
    get_unique_months,
    get_top_products,
)

st.title("📊 Online Store Dashboard")

# -----------------------
# 1. DATA INPUT
# -----------------------
df = None

option = st.sidebar.radio("Data Source", ["Upload File", "URL"])

if option == "Upload File":
    file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    if file:
        df = load_data(file)

elif option == "URL":
    url = st.text_input("Enter URL")
    if url:
        df = load_data(url)

# -----------------------
# 2. STOP IF NO DATA
# -----------------------
if df is None:
    st.info("Please upload or load data")
    st.stop()

# -----------------------
# 3. PROCESS DATA
# -----------------------
df = clean_data(df)
df = prepare_data(df)

# -----------------------
# 4. FILTERS
# -----------------------
st.sidebar.header("🔎 Filters")

# Country filter
if "Country" in df.columns:
    countries = st.sidebar.multiselect(
        "Select Country",
        options=get_unique_countries(df),
        default=get_unique_countries(df)
    )
    df = df[df["Country"].isin(countries)]

# Month filter
if "InvoiceMonth" in df.columns:
    months = st.sidebar.multiselect(
        "Select Month",
        options=get_unique_months(df),
        default=get_unique_months(df)
    )
    df = df[df["InvoiceMonth"].isin(months)]

# Product filter
if "Description" in df.columns:
    products = st.sidebar.multiselect(
        "Select Top Products",
        options=get_top_products(df)
    )

    if products:
        df = df[df["Description"].isin(products)]

# -----------------------
# 5. SHOW DATA
# -----------------------
st.dataframe(df.head())