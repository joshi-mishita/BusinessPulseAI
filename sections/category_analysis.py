import streamlit as st
import plotly.express as px


def render_category_analysis(df):

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

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )

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
        paper_bgcolor="#FFFFFF",
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
                color="#24324A",
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
                color="#24324A",
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

    return category_profit