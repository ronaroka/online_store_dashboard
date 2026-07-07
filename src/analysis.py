import pandas as pd
import streamlit as st

@st.cache_data
def prepare_data(df):
    df = df.copy()

    df["TotalPrice"] = df["Quantity"] * df["Price"]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

    return df


@st.cache_data
def get_unique_countries(df):
    return sorted(df["Country"].dropna().unique())


@st.cache_data
def get_unique_months(df):
    return sorted(df["InvoiceMonth"].dropna().unique())


@st.cache_data
def get_top_products(df):
    return df["Description"].dropna().value_counts().index[:50].tolist()