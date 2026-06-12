import pdfplumber
from docx import Document


def extract_resume_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):

        text = ""

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    elif uploaded_file.name.endswith(".docx"):

        doc = Document(uploaded_file)

        text = "\n".join(
            [para.text for para in doc.paragraphs]
        )

        return text

    return ""