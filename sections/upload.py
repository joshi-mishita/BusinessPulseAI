import streamlit as st

def render_upload_section():

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

    return uploaded_file