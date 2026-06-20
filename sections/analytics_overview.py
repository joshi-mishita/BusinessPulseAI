import streamlit as st

def render_analytics_overview():
    st.write("")
    st.write("")

    st.markdown(
        """
        <h2 style="
        color:#24324A;
        font-size:36px;
        font-weight:700;
        margin-bottom:25px;
        ">
        Analytics Overview
        </h2>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="
        background:#FCE5DB;
        padding:30px;
        border-radius:28px;
        height:260px;
        ">
            <h3 style="color:#24324A;">Top Category</h3>
            <h1 style="color:#24324A;">Technology</h1>
            <p style="color:#4B5563;">
            Highest profit generating category.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
        background:#DDEBDF;
        padding:30px;
        border-radius:28px;
        height:260px;
        ">
            <h3 style="color:#24324A;">Best Region</h3>
            <h1 style="color:#24324A;">West</h1>
            <p style="color:#4B5563;">
            Leading region by profitability.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    with col3:
        st.markdown("""
        <div style="
        background:#E8DDF9;
        padding:30px;
        border-radius:28px;
        height:260px;
        ">
            <h3 style="color:#24324A;">Opportunity Area</h3>
            <h1 style="color:#24324A;">Central</h1>
            <p style="color:#4B5563;">
            Lowest regional contribution.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="
        background:#DCEBFA;
        padding:30px;
        border-radius:28px;
        height:260px;
        ">
            <h3 style="color:#24324A;">Recommendation</h3>
            <p style="
            color:#4B5563;
            font-size:18px;
            line-height:1.8;
            margin-top:35px;
            ">
            Focus marketing efforts on underperforming regions and expand investment in high-margin product categories.
            </p>
        </div>
        """, unsafe_allow_html=True)
