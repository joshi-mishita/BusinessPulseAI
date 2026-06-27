import streamlit as st

def load_css(): 
    st.markdown("""
    <style>

    /* Main App */
    .stApp{
        background-color:#F7F5F2;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background-color:#FFFFFF;
        border-right:1px solid #EAEAEA;
    }

    /* Sidebar Text */
    section[data-testid="stSidebar"]{
        background-color:#1F1F1F;
        border-right:1px solid #EAEAEA;
        width:280px !important;
    }

    /* Navigation Items */
    .sidebar-nav{
        font-size:22px;
        color:#24324A;
        padding:12px 16px;
        border-radius:14px;
        margin-bottom:10px;
        transition:all 0.25s ease;
        cursor:pointer;
    }

    .sidebar-nav:hover{
        background:#E8DDF9;
        transform:translateX(6px);
    }

    /* Remove Streamlit Branding */
    #MainMenu{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    /* Hero Title */
    .hero-title{
        font-size:60px;
        font-weight:700;
        color:#24324A;
        margin-bottom:0px;
    }

    /* Hero Subtitle */
    .hero-subtitle{
        font-size:22px;
        font-weight:500;
        color:#4B5563;
        margin-top:0px;
    }

    /* KPI Cards */
    .kpi-card{
        padding:25px;
        border-radius:24px;
        text-align:left;
        box-shadow:0px 4px 20px rgba(0,0,0,0.05);
        height:160px;
        transition:all 0.25s ease;
    }

    .kpi-card:hover{
        transform:translateY(-5px);
        box-shadow:0px 12px 30px rgba(0,0,0,0.08);
    }

    /* KPI Label */
    .kpi-label{
        font-size:16px;
        color:#64748B;
    }

    /* KPI Value */
    .kpi-value{
        font-size:42px;
        font-weight:700;
        color:#24324A;
        margin-top:20px;
    }

    /* Card Colors */
    .blue{
        background:#DCEBFA;
    }

    .peach{
        background:#FCE5DB;
    }

    .green{
        background:#DDEBDF;
    }

    .purple{
        background:#E8DDF9;
    }

    /* Upload Area */
    [data-testid="stFileUploader"]{
        background:#FFFFFF;
        border:1px solid #E8E3DD;
        border-radius:28px;
        padding:25px;
        box-shadow:0px 8px 24px rgba(0,0,0,0.04);
    }

    /*File Upload*/
    [data-testid="stFileUploader"] label{
        display:none;
    }

    </style>
    """, unsafe_allow_html=True)