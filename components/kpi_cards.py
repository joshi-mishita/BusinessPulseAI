import streamlit as st

def render_kpi_cards(
    revenue,
    profit,
    customers,
    health
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class='kpi-card blue'>
            <div class='kpi-label'>Revenue</div>
            <div class='kpi-value'>{revenue}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='kpi-card peach'>
            <div class='kpi-label'>Profit</div>
            <div class='kpi-value'>{profit}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='kpi-card green'>
            <div class='kpi-label'>Customers</div>
            <div class='kpi-value'>{customers}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='kpi-card purple'>
            <div class='kpi-label'>Health Score</div>
            <div class='kpi-value'>{health}</div>
        </div>
        """, unsafe_allow_html=True)