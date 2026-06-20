import streamlit as st

def render_business_health():

    st.write("")
    st.write("")

    st.markdown("""
    <style>
    .metric-card {
        padding: 25px;
        border-radius: 28px;
        height: 280px;
    }

    .metric-card h4{
        margin:0;
        color:#5B6475;
        font-size:18px;
        font-weight:500;
    }

    .metric-card h1{
        margin-top:40px;
        margin-bottom:0px;
        color:#24324A;
        font-size:52px;
        font-weight:700;
        line-height:1;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style="
    color:#24324A;
    font-size:42px;
    font-weight:700;
    margin-bottom:25px;
    ">
    Business Health
    </h2>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card" style="background:#DCEBFA;">
            <h4>Orders</h4>
            <h1>9,994</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card" style="background:#FCE5DB;">
            <h4>Avg Order Value</h4>
            <h1>$229</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card" style="background:#DDEBDF;">
            <h4>Profit Margin</h4>
            <h1>12.5%</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card" style="background:#E8DDF9;">
            <h4>Ship Time</h4>
            <h1>4.0 Days</h1>
        </div>
        """, unsafe_allow_html=True)