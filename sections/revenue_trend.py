import streamlit as st

def render_revenue_trend(fig):

    st.write("")
    st.write("")

    st.markdown("""
    <h2 style="
    color:#24324A;
    margin-top:40px;
    margin-bottom:20px;
    ">
    Revenue Trend
    </h2>
    """, unsafe_allow_html=True)

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="revenue_trend_chart"
    )