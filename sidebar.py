# import streamlit as st

# def render_sidebar():

#     st.sidebar.markdown(
#         """
#         <h1 style='
#             color:#FFFFFF;
#             font-size:24px;
#             font-weight:700;
#             margin-bottom:0px;
#         '>
#         BusinessPulse AI
#         </h1>
#         """,
#         unsafe_allow_html=True
#     )

#     st.sidebar.markdown(
#         """
#         <p style='
#             color:#94A3B8;
#             font-size:20px;
#             margin-top:0px;
#             margin-bottom:35px;
#         '>
#         Analytics & Insights Dashboard
#         </p>
#         """,
#         unsafe_allow_html=True
#     )

#     page = st.sidebar.radio(
#         "",
#         [
#             "Dashboard",
#             "Revenue Trend",
#             "Business Insights",
#             "Analytics Overview",
#             "Business Health",
#             "Category Analysis",
#             "Category Insights"
#         ]
#     )

#     return page