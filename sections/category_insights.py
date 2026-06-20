import streamlit as st


def render_category_insights(category_profit):

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

    # ==========================
    # Top Category Card
    # ==========================
    with c1:
        st.markdown(
f"""
<div style="
background:#FCE5DB;
padding:35px;
border-radius:28px;
height:220px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="
color:#5B6475;
font-size:20px;
font-weight:500;
text-align:center;
margin-bottom:25px;
">
Top Category
</div>

<div style="
color:#24324A;
font-size:48px;
font-weight:700;
text-align:center;
">
{top_category}
</div>

<div style="
color:#6B7280;
font-size:15px;
text-align:center;
margin-top:20px;
">
Highest profit generating category
</div>

</div>
""",
unsafe_allow_html=True
        )

    # ==========================
    # Opportunity Category Card
    # ==========================
    with c2:
        st.markdown(
f"""
<div style="
background:#E8DDF9;
padding:35px;
border-radius:28px;
height:220px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="
color:#5B6475;
font-size:20px;
font-weight:500;
text-align:center;
margin-bottom:25px;
">
Opportunity Category
</div>

<div style="
color:#24324A;
font-size:48px;
font-weight:700;
text-align:center;
">
{opportunity_category}
</div>

<div style="
color:#6B7280;
font-size:15px;
text-align:center;
margin-top:20px;
">
Lowest profit contribution
</div>

</div>
""",
unsafe_allow_html=True
        )

    st.write("")

    # ==========================
    # Recommendation Card
    # ==========================
    st.markdown(
f"""
<div style="
background:#DCEBFA;
padding:35px;
border-radius:28px;
">

<div style="
color:#24324A;
font-size:28px;
font-weight:700;
margin-bottom:20px;
">
Recommendation
</div>

<div style="
color:#24324A;
font-size:18px;
line-height:1.9;
font-weight:500;
">

Increase inventory allocation and marketing focus toward
<b>{top_category}</b>.
Review pricing strategy, discounts and product mix within
<b>{opportunity_category}</b>
to improve profitability and overall business performance.

</div>

</div>
""",
unsafe_allow_html=True
    )