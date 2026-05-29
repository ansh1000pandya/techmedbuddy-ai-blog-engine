import re

from app.services.llm_router import (
    generate_llm_response
)

from app.prompts.reviewer_prompt import (
    get_reviewer_prompt
)


def review_section(
    topic,
    section_title,
    section_content
):

    prompt = get_reviewer_prompt(
        topic,
        section_title,
        section_content
    )

    response = generate_llm_response(
        prompt
    )

    print("\n========== REVIEW RESPONSE ==========\n")

    print(response)

    score = 0
    feedback = ""

    try:

        score_match = re.search(
            r"SCORE:\s*(\d+)",
            response
        )

        if score_match:

            score = int(
                score_match.group(1)
            )

        feedback_match = re.search(
            r"FEEDBACK:(.*)",
            response,
            re.DOTALL
        )

        if feedback_match:

            feedback = (
                feedback_match.group(1).strip()
            )

    except Exception as e:

        print(
            "\nReviewer Parse Error:\n",
            e
        )

    return {
        "score": score,
        "feedback": feedback
    }