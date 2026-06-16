def recommend_jobs(skills):

    jobs = []

    skills = [s.lower() for s in skills]

    if "python" in skills:
        jobs.append("Python Developer")

    if "machine learning" in skills:
        jobs.append("Machine Learning Engineer")

    if "nlp" in skills:
        jobs.append("NLP Engineer")

    if "streamlit" in skills:
        jobs.append("AI Application Developer")

    if "pandas" in skills:
        jobs.append("Data Analyst")

    return list(set(jobs))