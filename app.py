
import streamlit as st
import pandas as pd

from modules.resume_parser import extract_resume_text
from modules.matcher import calculate_match_score
from modules.skill_extractor import extract_skills
from modules.feedback import generate_feedback
from modules.interview_generator import generate_questions
from modules.groq_feedback import generate_ai_feedback
from modules.report_generator import generate_report

from modules.ui_components import (
    score_card,
    hero_section
)


def load_css():
    with open(
        "assets/style.css",
        "r",
        encoding="utf-8"
    ) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

load_css()

# ==========================
# HEADER
# ==========================

hero_section()

# ==========================
# DEFAULT VARIABLES
# ==========================

score = 0
ats_score = 0
resume_text = ""
matching_skills = []
missing_skills = []
feedback = []
questions = []
ai_feedback = ""

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("⚙️ Settings")

    api_key = st.text_input(
        "Groq API Key",
        type="password"
    )

    st.info(
        "Enter your Groq API Key here."
    )

# ==========================
# INPUTS
# ==========================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

jd_text = st.text_area(
    "Paste Job Description",
    height=200
)

# ==========================
# ANALYZE BUTTON
# ==========================

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

if analyze:

    if uploaded_file and jd_text:

        # Resume Text Extraction
        resume_text = extract_resume_text(
            uploaded_file
        )

        # Resume Match Score
        score = calculate_match_score(
            resume_text,
            jd_text
        )

        # Skills Database
        skills_df = pd.read_csv(
            "data/skills_database.csv",
            header=None
        )

        skills_list = skills_df[0].tolist()

        # Skill Extraction
        resume_skills = extract_skills(
            resume_text,
            skills_list
        )

        jd_skills = extract_skills(
            jd_text,
            skills_list
        )

        # Matching Skills
        matching_skills = list(
            set(resume_skills) &
            set(jd_skills)
        )

        # Missing Skills
        missing_skills = list(
            set(jd_skills) -
            set(resume_skills)
        )

        # ATS Score
        ats_score = round(
            (
                score * 0.8
                +
                (
                    len(matching_skills)
                    /
                    max(len(jd_skills), 1)
                ) * 20
            ),
            2
        )

        ats_score = min(
            ats_score,
            100
        )

        feedback = generate_feedback(
            missing_skills
        )

        questions = generate_questions(
            matching_skills
        )

        # ==========================
        # SCORE CARDS
        # ==========================

        col1, col2 = st.columns(2)

        with col1:
            score_card(
                "🎯 Match Score",
                f"{score}%"
            )

        with col2:
            score_card(
                "📊 ATS Score",
                f"{ats_score}/100"
            )

        # ==========================
        # RESUME VIEWER
        # ==========================

        with st.expander(
            "📄 View Extracted Resume",
            expanded=False
        ):

            st.text_area(
                "Resume Content",
                resume_text,
                height=300
            )

        # ==========================
        # SKILLS SECTION
        # ==========================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "✅ Matching Skills"
            )

            if matching_skills:

                for skill in matching_skills:
                    st.success(skill)

            else:

                st.warning(
                    "No Matching Skills Found"
                )

        with col2:

            st.subheader(
                "❌ Missing Skills"
            )

            if missing_skills:

                for skill in missing_skills:
                    st.error(skill)

            else:

                st.success(
                    "No Missing Skills Found"
                )

        # ==========================
        # SKILLS FOUND
        # ==========================

        st.subheader(
            "📌 Skills Found In Resume"
        )

        st.write(
            resume_skills
        )

        # ==========================
        # TABS
        # ==========================

        tab1, tab2 = st.tabs(
            [
                "🤖 AI Analysis",
                "🎤 Interview Prep"
            ]
        )

        # ==========================
        # TAB 1
        # ==========================

        with tab1:

            st.subheader(
                "🤖 AI Resume Feedback"
            )

            for item in feedback:
                st.info(item)

            if api_key:

                st.subheader(
                    "🧠 Groq AI Resume Analysis"
                )

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    ai_feedback = generate_ai_feedback(
                        resume_text,
                        jd_text,
                        api_key
                    )

                    st.markdown(
                        ai_feedback
                    )

            else:

                ai_feedback = (
                    "Groq API Key Not Provided"
                )

                st.warning(
                    "Please enter Groq API Key."
                )

        # ==========================
        # TAB 2
        # ==========================

        with tab2:

            st.subheader(
                "🎤 Interview Questions"
            )

            if questions:

                for i, question in enumerate(
                    questions,
                    start=1
                ):

                    st.write(
                        f"{i}. {question}"
                    )

            else:

                st.info(
                    "No interview questions available."
                )

        # ==========================
        # PDF REPORT
        # ==========================

        generate_report(
            "resume_report.pdf",
            score,
            ats_score,
            matching_skills,
            missing_skills,
            feedback,
            questions,
            ai_feedback,
            resume_text.split("\n")[0]
            if resume_text else "Candidate"
        )

        with open(
            "resume_report.pdf",
            "rb"
        ) as file:

            st.download_button(
                label="📥 Download Report",
                data=file,
                file_name="Resume_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    else:

        st.error(
            "Please upload a resume and paste a job description."
        )

