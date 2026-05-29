def get_reviewer_prompt(
    topic,
    section_title,
    section_content
):

    return f"""
Review this section.

Give:
1. SCORE out of 10
2. Short feedback

SECTION:
{section_content}
"""