# import streamlit as st
# import pandas as pd

# from analytics.kpi import calculate_kpis
# from analytics.health_score import calculate_health_score
# from analytics.recommendation import get_recommendations
# from analytics.trend_analysis import get_monthly_sales
# from analytics.category_analysis import get_category_profit
# from analytics.region_analysis import get_region_profit
# from analytics.business_summary import generate_business_summary

# # ==================================
# # Page Configuration
# # ==================================

# st.set_page_config(
#     page_title="BusinessPulse AI",
#     layout="wide"
# )

# # ==================================
# # Title
# # ==================================

# st.title("📊 BusinessPulse AI")

# st.write(
#     "Upload a business dataset and get instant business analytics."
# )

# # ==================================
# # File Upload
# # ==================================

# uploaded_file = st.file_uploader(
#     "Upload CSV File",
#     type=["csv"]
# )

# # ==================================
# # Main Dashboard
# # ==================================

# if uploaded_file:

#     df = pd.read_csv(
#         uploaded_file,
#         encoding="latin1"
#     )

#     # ==================================
#     # Tabs
#     # ==================================

#     tab1, tab2, tab3, tab4, tab5 = st.tabs(
#         [
#             "📊 Overview",
#             "📈 Trends",
#             "📂 Categories",
#             "🌎 Regions",
#             "🤖 AI Analyst"
#         ]
#     )   

#     # ==================================
#     # OVERVIEW TAB
#     # ==================================

#     with tab1:

#         st.header("Business Overview")

#         # KPI Section

#         kpis = calculate_kpis(df)

#         # First Row

#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.metric(
#                 "Revenue",
#                 f"${kpis['Revenue']:,.0f}"
#             )

#         with col2:
#             st.metric(
#                 "Profit",
#                 f"${kpis['Profit']:,.0f}"
#             )

#         with col3:
#             st.metric(
#                 "Customers",
#                 f"{kpis['Customers']:,}"
#             )

#         # Second Row

#         col4, col5, col6 = st.columns(3)

#         with col4:
#             st.metric(
#                 "Orders",
#                 f"{kpis['Orders']:,}"
#             )

#         with col5:
#             st.metric(
#                 "Profit Margin",
#                 f"{kpis['Profit Margin']}%"
#             )

#         with col6:
#             st.metric(
#                 "Average Order Value",
#                 f"${kpis['Average Order Value']:,.2f}"
#             )
            
#         st.divider()

#         # Health Score

#         score = calculate_health_score(df)

#         st.subheader("Business Health Score")

#         st.progress(score / 100)

#         st.metric(
#             "Health Score",
#             score
#         )

#         if score >= 80:

#             st.success(
#                 "Business Status: Excellent"
#             )

#         elif score >= 60:

#             st.info(
#                 "Business Status: Healthy"
#             )

#         elif score >= 40:

#             st.warning(
#                 "Business Status: Needs Attention"
#             )

#         else:

#             st.error(
#                 "Business Status: At Risk"
#             )

#         st.divider()

#         # Recommendations

#         st.subheader("Business Recommendations")

#         recommendations = get_recommendations(df)

#         for rec in recommendations:

#             st.write("✅", rec)

#     # ==================================
#     # TRENDS TAB
#     # ==================================

#     with tab2:

#         st.header("Revenue Trends")

#         monthly_sales = get_monthly_sales(df)

#         st.subheader("📈 Monthly Revenue Trend")

#         st.line_chart(
#             monthly_sales.set_index(
#                 "Order Date"
#             )
#         )

#     # ==================================
#     # CATEGORY TAB
#     # ==================================

#     with tab3:

#         st.header("Category Analysis")

#         category_profit = get_category_profit(df)

#         st.subheader("📊 Category Performance")

#         st.bar_chart(category_profit)

#         best_category = category_profit.idxmax()
#         worst_category = category_profit.idxmin()

#         st.success(
#             f"🏆 Best Category: {best_category}"
#         )

#         st.warning(
#             f"⚠ Lowest Performing Category: {worst_category}"
#         )

#     # ==================================
#     # REGION TAB
#     # ==================================

#     with tab4:

#         st.header("Region Analysis")

#         region_profit = get_region_profit(df)

#         st.subheader("🌎 Region Performance")

#         st.bar_chart(region_profit)

#         best_region = region_profit.idxmax()
#         worst_region = region_profit.idxmin()

#         st.success(
#             f"🏆 Best Region: {best_region}"
#         )

#         st.warning(
#             f"⚠ Lowest Performing Region: {worst_region}"
#         )
    
#     # ==================================
#     # AI ANALYST TAB
#     # ==================================

#     with tab5:

#         st.header("🤖 AI Business Analyst")

#         summary = generate_business_summary(
#             score,
#             best_category,
#             worst_category,
#             best_region,
#             worst_region
#         )

#         st.subheader("Executive Summary")

#         for point in summary:

#             st.info(point)










import streamlit as st
import pandas as pd
import plotly.express as px

from analytics.kpi import calculate_kpis
from analytics.trend_analysis import get_monthly_sales
from analytics.category_analysis import get_category_profit


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="BusinessPulse AI",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

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
    background-color:#FFFFFF;
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

# =====================================
# SIDEBAR
# =====================================

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

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class='hero-title'>
BusinessPulse AI
</div>

<div class='hero-subtitle'>
Transform business data into actionable insights.
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# FILE UPLOAD
# =====================================

st.markdown("""
<h2 style="
color:#24324A;
font-weight:700;
margin-bottom:15px;
">
Upload Dataset
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
color:#6B7280;
font-size:18px;
margin-bottom:10px;
">
Upload your business dataset to generate insights.
</p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "",
    type=["csv"]
)

st.write("")

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

kpis = calculate_kpis(df)

# KPI Values

revenue = f"${kpis['Revenue']/1000000:.2f}M"
profit = f"${kpis['Profit']/1000:.0f}K"
customers = f"{kpis['Customers']}"
health = "73"

# KPI Cards

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
    

# =====================================
# REVENUE TREND
# =====================================

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

monthly_sales = get_monthly_sales(df)

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

st.plotly_chart(
    fig,
    use_container_width=True,
    key="revenue_trend_chart"
)

# =====================================
# BUSINESS INSIGHTS
# =====================================

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
    

# =====================================
# ANALYTICS OVERVIEW
# =====================================

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


# =====================================
# BUSINESS HEALTH
# =====================================

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






# =====================================
# CATEGORY ANALYSIS
# =====================================

st.write("")
st.write("")

st.markdown("""
<h2 style="
color:#24324A;
font-size:42px;
font-weight:700;
margin-bottom:25px;
">
Category Analysis
</h2>
""", unsafe_allow_html=True)

# Category Profit Data
category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .reset_index()
    .sort_values("Profit", ascending=False)
)


# BAR CHART

fig_category = px.bar(
    category_profit,
    x="Category",
    y="Profit",
    color="Category",
    text="Profit",
    color_discrete_sequence=[
        "#DCEBFA",
        "#FCE5DB",
        "#DDEBDF"
    ]
)

fig_category.update_traces(
    texttemplate='$%{text:,.0f}',
    textposition='outside',
    marker_line_width=0
)

fig_category.update_layout(
    title="Profit by Category",
    title_font_size=30,
    title_font_color="#24324A",

    height=550,

    paper_bgcolor="#FFFFFF",   # CHANGE THIS
    plot_bgcolor="#FFFFFF",

    margin=dict(
        l=30,
        r=30,
        t=80,
        b=30
    ),

    showlegend=False,

    font=dict(
        color="#24324A",
        size=15
    ),

    xaxis=dict(
        title="Category",
        title_font=dict(
            color="#24324A",   # Category title color
            size=18
        ),
        showgrid=False,
        tickfont=dict(
            size=16,
            color="#24324A"
        )
    ),

    yaxis=dict(
        title="Profit ($)",
        title_font=dict(
            color="#24324A",   # Profit title color
            size=18
        ),
        gridcolor="#EAEAEA",
        gridwidth=1,
        zeroline=False,
        tickfont=dict(
            size=15,
            color="#24324A"
        )
    )
)

st.plotly_chart(
    fig_category,
    use_container_width=True,
    key="category_chart"
)


# =====================================
# CATEGORY INSIGHTS
# =====================================

top_category = category_profit.iloc[0]["Category"]
opportunity_category = category_profit.iloc[-1]["Category"]

st.write("")
st.write("")

st.markdown("""
<h2 style="
color:#24324A;
font-size:38px;
font-weight:700;
margin-bottom:25px;
">
Category Insights
</h2>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

# Top Category
with c1:
    st.markdown(f"""
    <div style="
    background:#FCE5DB;
    padding:30px;
    border-radius:28px;
    height:180px;
    ">
        <div style="
        color:#5B6475;
        font-size:20px;
        font-weight:500;
        ">
        Top Category
        </div>

        <div style="
        color:#24324A;
        font-size:38px;
        font-weight:700;
        margin-top:30px;
        ">
        {top_category}
        </div>

        <div style="
        color:#6B7280;
        font-size:15px;
        margin-top:10px;
        ">
        Highest profit generating category
        </div>
    </div>
    """, unsafe_allow_html=True)

# Opportunity Category
with c2:
    st.markdown(f"""
    <div style="
    background:#E8DDF9;
    padding:30px;
    border-radius:28px;
    height:180px;
    ">
        <div style="
        color:#5B6475;
        font-size:20px;
        font-weight:500;
        ">
        Opportunity Category
        </div>

        <div style="
        color:#24324A;
        font-size:38px;
        font-weight:700;
        margin-top:30px;
        ">
        {opportunity_category}
        </div>

        <div style="
        color:#6B7280;
        font-size:15px;
        margin-top:10px;
        ">
        Lowest profit contribution
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Recommendation Card
st.markdown(f"""
<div style="
background:#DCEBFA;
padding:30px;
border-radius:28px;
">

<div style="
color:#24324A;
font-size:24px;
font-weight:700;
margin-bottom:15px;
">
Recommendation
</div>

<div style="
color:#4B5563;
font-size:17px;
line-height:1.8;
">
Increase inventory allocation and marketing focus toward
<b>{top_category}</b>.
Review pricing strategy, discounts and product mix within
<b>{opportunity_category}</b>
to improve profitability and overall business performance.
</div>

</div>
""", unsafe_allow_html=True)