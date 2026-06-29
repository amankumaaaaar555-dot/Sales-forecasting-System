"""
eda.py

Exploratory Data Analysis (EDA) module for the
Sales Forecasting System.

Responsibilities
----------------
- Generate sales trend
- Generate entity performance chart
- Generate correlation matrix
- Generate feature distributions
- Return all EDA results

Author: Aman Kumar
"""

import logging

import pandas as pd
import plotly.express as px

from dataset_info import generate_dataset_summary

from config import (
    DATE_COLUMN,
    TARGET_COLUMN,
    ID_COLUMNS,
    NUMERICAL_COLUMNS
)

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# Sales Trend
# ==========================================================

def generate_sales_trend(df: pd.DataFrame):

    logger.info("Generating sales trend...")

    sales_df = (
        df.groupby(DATE_COLUMN)[TARGET_COLUMN]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales_df,
        x=DATE_COLUMN,
        y=TARGET_COLUMN,
        title="Sales Trend Over Time"
    )

    return fig


# ==========================================================
# Entity Performance
# ==========================================================

def generate_entity_performance(df: pd.DataFrame):

    logger.info("Generating entity performance...")

    entity_column = ID_COLUMNS[0]

    performance = (
        df.groupby(entity_column)[TARGET_COLUMN]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        performance,
        x=entity_column,
        y=TARGET_COLUMN,
        title=f"Average {TARGET_COLUMN} by {entity_column}"
    )

    return fig


# ==========================================================
# Correlation Matrix
# ==========================================================

def generate_correlation_matrix(df: pd.DataFrame):

    logger.info("Generating correlation matrix...")

    correlation_columns = NUMERICAL_COLUMNS + [TARGET_COLUMN]

    corr = df[correlation_columns].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Matrix"
    )

    return fig


# ==========================================================
# Feature Distributions
# ==========================================================

def generate_feature_distributions(df: pd.DataFrame):

    logger.info("Generating feature distributions...")

    figures = {}

    columns = NUMERICAL_COLUMNS + [TARGET_COLUMN]

    for column in columns:

        fig = px.histogram(
            df,
            x=column,
            nbins=30,
            title=f"{column} Distribution"
        )

        figures[column] = fig

    return figures


# ==========================================================
# Run Complete EDA
# ==========================================================

def run_eda(df: pd.DataFrame):

    logger.info("=" * 60)
    logger.info("Running Exploratory Data Analysis...")
    logger.info("=" * 60)

    results = {

        "summary": generate_dataset_summary(df),

        "sales_trend":
            generate_sales_trend(df),

        "entity_performance":
            generate_entity_performance(df),

        "correlation_matrix":
            generate_correlation_matrix(df),

        "feature_distributions":
            generate_feature_distributions(df)

    }

    logger.info("EDA completed successfully.")

    return results