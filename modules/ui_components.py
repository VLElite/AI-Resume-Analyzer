import streamlit as st


def score_card(title, value):

    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="score">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def hero_section():

    st.markdown(
        """
        <div class="hero">
            <h1>📄 AI Resume Analyzer</h1>
            <p>
                AI-Powered Resume Evaluation, ATS Optimization &
                Interview Preparation
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )