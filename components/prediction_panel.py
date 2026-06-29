"""
prediction_panel.py

Prediction panel component for the
Sales Forecasting System.

Responsibilities
----------------
- Display forecast summary
- Display forecast table
- Display forecast chart
- Download forecast

Author: Aman Kumar
"""

import streamlit as st
import plotly.express as px

from config import DATE_COLUMN


# ==========================================================
# Prediction Panel
# ==========================================================

def show_prediction_panel(forecast_df):
    """
    Display forecast results.

    Parameters
    ----------
    forecast_df : pd.DataFrame
        Forecast dataframe returned by predictor.py
    """

    st.header("🔮 Sales Forecast")

    st.markdown(
        """
        Future sales generated using the selected
        forecasting model.
        """
    )

    # ======================================================
    # Summary Statistics
    # ======================================================

    total_predictions = len(forecast_df)

    average_sales = forecast_df["Predicted_Sales"].mean()

    minimum_sales = forecast_df["Predicted_Sales"].min()

    maximum_sales = forecast_df["Predicted_Sales"].max()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Forecast Periods",
            total_predictions
        )

        st.metric(
            "Average Forecast",
            f"{average_sales:,.2f}"
        )

    with col2:

        st.metric(
            "Minimum Forecast",
            f"{minimum_sales:,.2f}"
        )

        st.metric(
            "Maximum Forecast",
            f"{maximum_sales:,.2f}"
        )

    st.divider()

    # ======================================================
    # Forecast Table
    # ======================================================

    st.subheader("📄 Forecast Table")

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Forecast Chart
    # ======================================================

    st.subheader("📈 Forecast Trend")

    fig = px.line(
        forecast_df,
        x=DATE_COLUMN,
        y="Predicted_Sales",
        markers=True,
        title="Future Sales Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Download Forecast
    # ======================================================

    csv = forecast_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name="sales_forecast.csv",
        mime="text/csv"
    )