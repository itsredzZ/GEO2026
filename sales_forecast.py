import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col2:
    df_forecast = pd.read_excel("Future predicted data 2026.xlsx")

    df_forecast["date"] = pd.to_datetime(
        df_forecast["YEAR"].astype(str) + "-" +
        df_forecast["MONTH"].astype(str) + "-01"
    )

    df_forecast = df_forecast.sort_values("date")

    df_forecast["month_year"] = df_forecast["date"].dt.strftime("%b %Y")
    df_forecast["month_year"] = pd.Categorical(
        df_forecast["month_year"],
        categories=df_forecast["month_year"].unique(),
        ordered=True
    )

    st.title("Sales Forecast 2026")

    st.bar_chart(
        data=df_forecast,
        x="month_year",
        y="Prediction (SUM OF QTY)"
    )

with col1:
    df_history = pd.read_excel("Total quantity monthly.xlsx")

    df_history["date"] = pd.to_datetime(
        df_history["YEAR"].astype(str) + "-" +
        df_history["MONTH"].astype(str) + "-01"
    )

    df_history = df_history.sort_values("date")

    df_history["month_year"] = df_history["date"].dt.strftime("%b %Y")
    df_history["month_year"] = pd.Categorical(
        df_history["month_year"],
        categories=df_history["month_year"].unique(),
        ordered=True
    )

    st.title("History of Sales 2023–2025")

    st.bar_chart(
        data=df_history,
        x="month_year",
        y="SUM of QTY"
    )