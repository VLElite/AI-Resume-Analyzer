def generate_questions(skills):

    questions = []

    if "Python" in skills:

        questions.extend([
            "What are Python decorators?",
            "Difference between List and Tuple?",
            "What is a Lambda Function?"
        ])

    if "Machine Learning" in skills:

        questions.extend([
            "What is Overfitting?",
            "Difference between Supervised and Unsupervised Learning?",
            "What is Cross Validation?"
        ])

    if "SQL" in skills:

        questions.extend([
            "What is a Primary Key?",
            "Difference between INNER JOIN and LEFT JOIN?",
            "What are SQL Indexes?"
        ])

    if "NLP" in skills:

        questions.extend([
            "What is Tokenization?",
            "What is Stemming?",
            "What is TF-IDF?"
        ])

    return questions