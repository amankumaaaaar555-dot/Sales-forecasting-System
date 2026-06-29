"""
validation_panel.py

Validation panel component for the
Sales Forecasting System.

Responsibilities
----------------
- Display validation status
- Display validation errors
- Display validation warnings

Author: Aman Kumar
"""

import streamlit as st


# ==========================================================
# Validation Panel
# ==========================================================

def show_validation_panel(report):
    """
    Display validation report.

    Parameters
    ----------
    report : ValidationReport
    """

    st.header("🛡️ Dataset Validation")

    # ------------------------------------------------------
    # Validation Status
    # ------------------------------------------------------

    if report.is_valid:

        st.success("Dataset validation passed successfully.")

    else:

        st.error("Dataset validation failed.")

    # ------------------------------------------------------
    # Errors
    # ------------------------------------------------------

    if report.errors:

        st.subheader("❌ Errors")

        for error in report.errors:

            st.error(error)

    # ------------------------------------------------------
    # Warnings
    # ------------------------------------------------------

    if report.warnings:

        st.subheader("⚠️ Warnings")

        for warning in report.warnings:

            st.warning(warning)

    st.divider()