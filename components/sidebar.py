import streamlit as st

def render_sidebar():
    st.sidebar.markdown(
        """
        <h1 style='
            color:#24324A;
            font-size:24px;
            font-weight:700;
            margin-bottom:30px;
        '>
        BusinessPulse AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div class='sidebar-nav'>Overview</div>",
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div class='sidebar-nav'>Analytics</div>",
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div class='sidebar-nav'>Forecast</div>",
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        "<div class='sidebar-nav'>Reports</div>",
        unsafe_allow_html=True
    )