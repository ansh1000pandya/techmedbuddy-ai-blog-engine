import re

from app.services.llm_router import (
    generate_llm_response
)


def extract_tutorial_score(review_text):

    numbers = re.findall(
        r"\d+",
        review_text
    )

    if len(numbers) > 0:

        try:

            score = int(numbers[0])

            return max(
                1,
                min(score, 10)
            )

        except:

            return 5

    return 5


def review_tutorial_section(

    topic,

    section,

    content

):

    review_prompt = f"""
    You are an elite biomedical
    educator and tutorial reviewer.

    Review this tutorial section.

    TOPIC:
    {topic}

    SECTION:
    {section}

    CONTENT:
    {content}

    Evaluate:

    1. Educational clarity
    2. Conceptual depth
    3. Beginner friendliness
    4. Biology relevance
    5. Clinical relevance
    6. Learning progression
    7. Tutorial quality
    8. Examples quality
    9. Practical usefulness
    10. Engagement quality

    STRICT RULES:

    - reject shallow explanations
    - reject generic tutorials
    - reject repetitive structure
    - reject weak educational flow
    - reject low-detail sections

    Return ONLY:

    SCORE: X/10

    FEEDBACK:
    concise educational feedback
    """

    review_output = (
        generate_llm_response(
            review_prompt
        )
    )

    score = (
        extract_tutorial_score(
            review_output
        )
    )

    return {

        "score": score,

        "feedback": review_output

    }