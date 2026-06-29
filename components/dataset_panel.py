"""
dataset_panel.py

Dataset panel component for the
Sales Forecasting System.

Responsibilities
----------------
- Display dataset preview
- Display dataset summary
- Display column names
- Display data types

Author: Aman Kumar
"""

import streamlit as st

from dataset_info import generate_dataset_summary


# ==========================================================
# Dataset Panel
# ==========================================================

def show_dataset_panel(df):
    """
    Display dataset preview and summary.

    Parameters
    ----------
    df : pandas.DataFrame
    """

    # ======================================================
    # Dataset Preview
    # ======================================================

    st.header("📄 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Dataset Summary
    # ======================================================

    summary = generate_dataset_summary(df)

    st.header("📊 Dataset Information")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", summary["Rows"])

    with col2:
        st.metric("Columns", summary["Columns"])

    with col3:
        st.metric("Duplicate Rows", summary["Duplicate Rows"])

    with col4:
        st.metric("Memory Usage", summary["Memory Usage"])

    st.divider()

    # ======================================================
    # Column Names
    # ======================================================

    st.subheader("📋 Column Names")

    st.write(summary["Column Names"])

    # ======================================================
    # Data Types
    # ======================================================

    st.subheader("🧾 Data Types")

    st.json(summary["Data Types"])

    # ======================================================
    # Missing Values
    # ======================================================

    st.subheader("⚠️ Missing Values")

    st.json(summary["Missing Values"])

    st.divider()