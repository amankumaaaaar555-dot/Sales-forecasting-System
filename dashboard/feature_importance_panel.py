"""
feature_importance_panel.py

Feature Importance Dashboard

Author: Aman Kumar
"""

import streamlit as st
import plotly.express as px


# ==========================================================
# Dashboard
# ==========================================================

def show_feature_importance_panel(
    importance_df
):
    """
    Display feature importance chart.
    """

    if importance_df is None:

        st.info(
            "Feature importance is not available for this model."
        )

        return

    st.divider()

    st.header("🧠 Explainable AI")

    st.write(
        "Feature importance generated from the trained model."
    )

    fig = px.bar(

        importance_df,

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance",

        text="Importance"

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.dataframe(

        importance_df,

        use_container_width=True,

        hide_index=True

    )