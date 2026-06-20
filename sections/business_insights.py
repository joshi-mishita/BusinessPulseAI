import streamlit as st

def render_business_insights():

    st.write("")
    st.write("")

    st.markdown("""
    <h2 style="
    color:#24324A;
    margin-top:40px;
    margin-bottom:20px;
    font-size:36px;
    font-weight:700;
    ">
    Business Insights
    </h2>
    """, unsafe_allow_html=True)

    left, right = st.columns([2,1])

    # =====================================
    # EXECUTIVE SUMMARY CARD
    # =====================================

    with left:

        st.markdown(f"""
        <div style="
        background:#FFFFFF;
        padding:35px;
        border-radius:28px;
        border:1px solid #ECE7E1;
        box-shadow:0px 6px 20px rgba(0,0,0,0.04);
        min-height:320px;
        ">

        <h3 style="
        color:#24324A;
        margin-top:0;
        font-size:28px;
        ">
        Executive Summary
        </h3>

        <div style="
        color:#4B5563;
        font-size:18px;
        line-height:2;
        ">

        • Revenue performance remains stable across major business segments.<br>

        • Customer acquisition continues to contribute positively to growth.<br>

        • Technology category generates the highest profitability.<br>

        • West region remains the strongest revenue contributor.<br>

        • Opportunity exists to improve performance in weaker regions.

        </div>

        </div>
        """,
        unsafe_allow_html=True)

    # =====================================
    # HEALTH SCORE CARD
    # =====================================

    with right:

        st.markdown("""
        <div style="
        background:#DDEBDF;
        padding:35px;
        border-radius:28px;
        min-height:320px;
        box-shadow:0px 6px 20px rgba(0,0,0,0.04);
        ">

        <h3 style="
        color:#24324A;
        margin-top:0;
        font-size:28px;
        ">
        Business Health
        </h3>

        <div style="
        font-size:72px;
        font-weight:700;
        color:#24324A;
        margin-top:20px;
        ">
        73
        </div>

        <div style="
        font-size:22px;
        color:#4B5563;
        margin-top:10px;
        ">
        Healthy Growth
        </div>

        <div style="
        margin-top:30px;
        background:#FFFFFF;
        padding:16px;
        border-radius:18px;
        color:#24324A;
        ">
        Strong profitability and positive growth indicators.
        </div>

        </div>
        """,
        unsafe_allow_html=True)