import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="BusinessPulse AI",
    page_icon="📊",
    layout="wide"
)


from analytics.kpi import calculate_kpis
from analytics.trend_analysis import get_monthly_sales

from components.styles import load_css
from components.kpi_cards import render_kpi_cards

from sections.upload import render_upload_section
from sections.revenue_trend import render_revenue_trend
from sections.business_insights import render_business_insights
from sections.analytics_overview import render_analytics_overview
from sections.business_health import render_business_health
from sections.category_analysis import render_category_analysis
from sections.category_insights import render_category_insights


load_css()

st.markdown(f"""
<div style="
text-align:right;
color:#6B7280;
font-size:16px;
font-weight:600;
margin-bottom:15px;
">
Last Updated • {pd.Timestamp.today().strftime("%d %b %Y")}
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:linear-gradient(
135deg,
#DCEBFA 0%,
#E8DDF9 100%
);
padding:45px;
border-radius:40px;
width:100%;
box-shadow:0px 10px 25px rgba(0,0,0,0.04);
margin-bottom:35px;
">

<div style="
color:#24324A;
font-size:78px;
font-weight:800;
line-height:1;
">
BusinessPulse AI
</div>

<div style="
color:#4B5563;
font-size:26px;
font-weight:600;
margin-top:25px;
">
Analytics & Insights Dashboard
</div>

<div style="
color:#6B7280;
font-size:18px;
margin-top:15px;
">
AI-Powered Business Intelligence Platform
</div>

</div>
""", unsafe_allow_html=True)


# =====================================
# FILE UPLOAD
# =====================================

uploaded_file = render_upload_section()

# =====================================
# KPI CARDS
# =====================================

if not uploaded_file:

    st.markdown("""
    <div style="
    background:#FFFFFF;
    padding:20px;
    border-radius:20px;
    border:1px solid #E5E7EB;
    color:#24324A;
    font-size:18px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.03);
    ">
    Upload a CSV dataset to begin analysis.
    </div>
    """, unsafe_allow_html=True)

    st.stop()

df = pd.read_csv(
    uploaded_file,
    encoding="latin1"
)

# =====================================
# FILTERS
# =====================================

st.markdown("""
<h2 style="
color:#24324A;
font-size:30px;
font-weight:700;
margin-top:25px;
margin-bottom:20px;
">
Filters
</h2>
""", unsafe_allow_html=True)

with st.container():

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        region = st.selectbox(
            "Region",
            ["All"] + sorted(df["Region"].unique().tolist())
        )

    with c2:
        category = st.selectbox(
            "Category",
            ["All"] + sorted(df["Category"].unique().tolist())
        )

    with c3:
        segment = st.selectbox(
            "Segment",
            ["All"] + sorted(df["Segment"].unique().tolist())
        )

    with c4:
        years = sorted(
            pd.to_datetime(df["Order Date"])
            .dt.year
            .unique()
            .tolist()
        )

        year = st.selectbox(
            "Year",
            ["All"] + years
        )

# =====================================
# APPLY FILTERS
# =====================================

filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == region
    ]

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

if segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == segment
    ]

if year != "All":

    filtered_df["Order Date"] = pd.to_datetime(
        filtered_df["Order Date"]
    )

    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.year == year
    ]

# =====================================
# KPI DATA
# =====================================

kpis = calculate_kpis(filtered_df)
# KPI Values

revenue = f"${kpis['Revenue']/1000000:.2f}M"
profit = f"${kpis['Profit']/1000:.0f}K"
customers = f"{kpis['Customers']}"
health = "73"

# KPI Cards

render_kpi_cards(
    revenue,
    profit,
    customers,
    health
)
    

# =====================================
# REVENUE TREND
# =====================================

monthly_sales = get_monthly_sales(filtered_df)

fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
)

fig.update_traces(
    line=dict(
        width=5,
        color="#5C7C8D"
    ),
    fill="tozeroy",
    fillcolor="rgba(156,205,216,0.15)"
)

fig.update_layout(
    height=450,

    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",

    font=dict(
        color="#24324A",
        size=14
    ),

    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    ),

    xaxis=dict(
        title="Month",
        title_font=dict(
            size=16,
            color="#24324A"
        ),
        tickfont=dict(
            size=13,
            color="#24324A"
        ),
        showgrid=False,
        showline=False
    ),

    yaxis=dict(
        title="Revenue ($)",
        title_font=dict(
            size=16,
            color="#24324A"
        ),
        tickfont=dict(
            size=13,
            color="#24324A"
        ),
        gridcolor="#E5E7EB",
        zeroline=False
    ),

    hoverlabel=dict(
        bgcolor="#24324A",
        font_size=14
    ),

    showlegend=False
)

render_revenue_trend(fig)

# =====================================
# BUSINESS INSIGHTS
# =====================================

render_business_insights()
    

# =====================================
# ANALYTICS OVERVIEW
# =====================================

render_analytics_overview()

# =====================================
# BUSINESS HEALTH
# =====================================

render_business_health()

# =====================================
# CATEGORY ANALYSIS
# =====================================

category_profit = render_category_analysis(filtered_df)


# =====================================
# CATEGORY INSIGHTS
# =====================================

render_category_insights(category_profit)