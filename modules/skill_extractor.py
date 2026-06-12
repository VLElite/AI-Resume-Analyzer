import re

def extract_skills(text, skills_list):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills