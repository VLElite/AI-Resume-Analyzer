from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime


def generate_report(
    filename,
    score,
    ats_score,
    matching_skills,
    missing_skills,
    feedback,
    questions,
    ai_feedback,
    candidate_name="Candidate"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # =====================
    # TITLE
    # =====================

    content.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    # =====================
    # CANDIDATE INFO
    # =====================

    content.append(
        Paragraph(
            f"<b>Candidate:</b> {candidate_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Date Generated:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================
    # PERFORMANCE SUMMARY
    # =====================

    content.append(
        Paragraph(
            "Performance Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Resume Match Score: {score}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"ATS Score: {ats_score}/100",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================
    # MATCHING SKILLS
    # =====================

    content.append(
        Paragraph(
            "Matching Skills",
            styles["Heading1"]
        )
    )

    for skill in matching_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 15)
    )

    # =====================
    # MISSING SKILLS
    # =====================

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading1"]
        )
    )

    for skill in missing_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 15)
    )

    # =====================
    # AI FEEDBACK
    # =====================

    content.append(
        Paragraph(
            "AI Resume Feedback",
            styles["Heading1"]
        )
    )

    for item in feedback:

        content.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 15)
    )

    # =====================
    # INTERVIEW QUESTIONS
    # =====================

    content.append(
        Paragraph(
            "Interview Questions",
            styles["Heading1"]
        )
    )

    for i, question in enumerate(
        questions,
        start=1
    ):

        content.append(
            Paragraph(
                f"{i}. {question}",
                styles["Normal"]
            )
        )

    content.append(
        PageBreak()
    )

    # =====================
    # GROQ AI ANALYSIS
    # =====================

    content.append(
        Paragraph(
            "Groq AI Analysis",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    lines = str(ai_feedback).split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Remove markdown symbols
        line = (
            line.replace("**", "")
                .replace("*", "")
                .replace("#", "")
        )

        content.append(
            Paragraph(
                line,
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 4)
        )

    # =====================
    # FOOTER
    # =====================

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Generated using AI Resume Analyzer",
            styles["Italic"]
        )
    )

    doc.build(content)