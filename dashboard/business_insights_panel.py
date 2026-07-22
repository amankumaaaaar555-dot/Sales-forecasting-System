"""
business_insights_panel.py

Enterprise Business Insights Dashboard

Author: Aman Kumar
"""

import streamlit as st


def show_business_insights_panel(insights):

    st.divider()

    st.header("📊 Business Insights Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🏆 Highest Sales Region",
            insights["highest_region"],
            f"₹ {insights['highest_region_sales']:,.2f}"
        )

    with col2:
        st.metric(
            "📉 Lowest Sales Region",
            insights["lowest_region"],
            f"₹ {insights['lowest_region_sales']:,.2f}"
        )

    st.markdown("---")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric(
            "💰 Total Sales",
            f"₹ {insights['total_sales']:,.2f}"
        )

    with col4:
        st.metric(
            "📈 Average Sale",
            f"₹ {insights['average_sales']:,.2f}"
        )

    with col5:
        st.metric(
            "🚀 Maximum Sale",
            f"₹ {insights['maximum_sales']:,.2f}"
        )

    st.markdown("---")

    col6, col7 = st.columns(2)

    with col6:
        st.metric(
            "📦 Best Selling Product",
            insights["best_product"],
            insights["best_product_quantity"]
        )

    with col7:
        st.metric(
            "💳 Most Used Payment",
            insights["top_payment_method"]
        )

    st.markdown("---")

    st.subheader("💡 Business Recommendations")

    st.success(
        f"Focus more sales efforts in **{insights['highest_region']}** as it currently generates the highest revenue."
    )

    st.info(
        f"Increase inventory for **{insights['best_product']}** because it has the highest demand."
    )

    st.warning(
        f"Review sales strategy in **{insights['lowest_region']}** to improve revenue."
    )