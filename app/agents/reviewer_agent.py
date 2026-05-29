import re

from app.services.llm_router import (
    generate_llm_response
)


def extract_score(review_text):

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


def review_generated_section(

    topic,

    section,

    content

):

    review_prompt = f"""
    You are a senior biomedical
    research reviewer and
    scientific editor.

    Evaluate this generated section.

    TOPIC:
    {topic}

    SECTION:
    {section}

    CONTENT:
    {content}

    Evaluate:

    1. Topic relevance
    2. Scientific accuracy
    3. Educational clarity
    4. Logical flow
    5. Technical depth
    6. Clinical relevance
    7. Writing quality
    8. Continuity with topic
    9. Lack of repetition
    10. Professional tone

    Give:

    SCORE: X/10

    FEEDBACK:
    - concise improvement feedback

    STRICT RULES:

    - harsh reviewer
    - reject weak writing
    - reject generic content
    - reject repetitive structure
    - reject shallow explanations
    """

    review_output = generate_llm_response(
        review_prompt
    )

    score = extract_score(
        review_output
    )

    return {

        "score": score,

        "feedback": review_output

    }