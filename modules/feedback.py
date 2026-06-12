def generate_feedback(missing_skills):

    feedback = []

    if "SQL" in missing_skills:
        feedback.append(
            "Add a SQL-based project to strengthen your database skills."
        )

    if "AWS" in missing_skills:
        feedback.append(
            "Learn AWS Cloud Practitioner and add a cloud project."
        )

    if "Docker" in missing_skills:
        feedback.append(
            "Learn Docker fundamentals and containerization."
        )

    if "NLP" in missing_skills:
        feedback.append(
            "Build an NLP project using Python."
        )

    if "Deep Learning" in missing_skills:
        feedback.append(
            "Add a Deep Learning project using TensorFlow or PyTorch."
        )

    if "Data Analysis" in missing_skills:
        feedback.append(
            "Work on a Data Analysis project using Pandas and NumPy."
        )

    if len(feedback) == 0:
        feedback.append(
            "Excellent Resume! Your skills align well with the job description."
        )

    return feedback