import pandas as pd
import streamlit as st

df = pd.read_excel("Future predicted data 2026.xlsx")

df["date"] = pd.to_datetime(
    df["YEAR"].astype(str) + "-" +
    df["MONTH"].astype(str) + "-01")

df = df.sort_values("date")

df["month_year"] = df["date"].dt.strftime("%b %Y")
df["month_year"] = pd.Categorical(
    df["month_year"],
    categories=df["month_year"].unique(),
    ordered=True
)

st.title("Sales Forecast 2026")

st.bar_chart(
    data=df,
    x="month_year",
    y="Prediction (SUM OF QTY)"
)
