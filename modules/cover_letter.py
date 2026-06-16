from groq import Groq


def generate_cover_letter(
    resume_text,
    job_description,
    api_key
):

    client = Groq(
        api_key=api_key
    )

    prompt = f"""
    Create a professional cover letter.

    Candidate Resume:
    {resume_text}

    Job Description:
    {job_description}

    Requirements:
    - Professional tone
    - 250-350 words
    - Highlight relevant skills
    - Mention why candidate fits the role
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content