"""
download_panel.py

Download Center for the
Sales Forecasting Analytics Platform.

Responsibilities
----------------
- Download Forecast CSV
- Download Model Comparison
- Download Evaluation Report
- Download Trained Model

Author: Aman Kumar
"""

from pathlib import Path

import pandas as pd
import streamlit as st


# ==========================================================
# Download Panel
# ==========================================================

def show_download_panel(
    forecast_df=None,
    comparison_df=None,
    evaluation_results=None,
    model_path=None
):
    """
    Display download buttons for generated artifacts.
    """

    st.divider()

    st.header("📥 Download Center")

    st.write(
        "Download reports, forecasts, and trained models."
    )

    # ======================================================
    # Forecast CSV
    # ======================================================

    if forecast_df is not None:

        csv = forecast_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇ Download Forecast CSV",
            data=csv,
            file_name="forecast.csv",
            mime="text/csv"
        )

    # ======================================================
    # Model Comparison Report
    # ======================================================

    if comparison_df is not None:

        csv = comparison_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇ Download Model Comparison",
            data=csv,
            file_name="model_comparison.csv",
            mime="text/csv"
        )

    # ======================================================
    # Evaluation Metrics
    # ======================================================

    if evaluation_results is not None:

        metrics_df = pd.DataFrame(
            [evaluation_results]
        )

        csv = metrics_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇ Download Evaluation Report",
            data=csv,
            file_name="evaluation_report.csv",
            mime="text/csv"
        )

    # ======================================================
    # Trained Model
    # ======================================================

    if model_path is not None:

        model_file = Path(model_path)

        if model_file.exists():

            with open(model_file, "rb") as file:

                st.download_button(
                    label="⬇ Download Trained Model",
                    data=file,
                    file_name=model_file.name,
                    mime="application/octet-stream"
                )

        else:

            st.warning(
                "⚠ Trained model file not found."
            )