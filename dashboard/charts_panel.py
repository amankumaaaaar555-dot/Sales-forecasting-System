"""
charts_panel.py

Enterprise Dashboard Charts

Author: Aman Kumar
"""

import streamlit as st
import plotly.express as px

from config import DATE_COLUMN


def show_charts_panel(df, forecast_df=None):

    st.header("📈 Enterprise Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Enterprise Revenue Trend")

        fig = px.line(
            df,
            x=DATE_COLUMN,
            y="Total_Amount",
            title="Revenue Over Time"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("Regional Performance")

        region_sales = (

            df.groupby("Region_Name")["Total_Amount"]

            .sum()

            .reset_index()

        )

        fig = px.bar(

            region_sales,

            x="Region_Name",

            y="Total_Amount",

            color="Region_Name",

            title="Revenue by Region"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    if forecast_df is not None:

        st.subheader("Future Revenue Forecast")

        fig = px.line(

            forecast_df,

            x=DATE_COLUMN,

            y="Predicted_Sales",

            markers=True,

            title="Forecasted Revenue"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )