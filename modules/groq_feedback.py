from groq import Groq


def generate_ai_feedback(
    resume_text,
    job_description,
    api_key
):

    try:

        client = Groq(
            api_key=api_key
        )

        prompt = f"""
        Analyze the following resume against the job description.

        Resume:
        {resume_text}

        Job Description:
        {job_description}

        Provide:

        1. Strengths
        2. Weaknesses
        3. Missing Skills
        4. Suggestions
        """

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:

        return str(e)