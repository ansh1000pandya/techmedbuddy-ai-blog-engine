from app.services.llm_router import (
    generate_llm_response
)

from app.prompts.tutorial_planner_prompt import (
    get_tutorial_planner_prompt
)


def generate_tutorial_outline(topic):

    planner_prompt = (
        get_tutorial_planner_prompt(
            topic
        )
    )

    response = generate_llm_response(
        planner_prompt
    )

    sections = []

    for line in response.split("\n"):

        line = line.strip()

        if line.startswith("Section"):

            sections.append(line)

    # fallback

    if len(sections) < 3:

        sections = [

            "Section 1: Foundations",

            "Section 2: Core Concepts",

            "Section 3: Advanced Applications"

        ]

    return sections