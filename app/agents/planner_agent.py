from app.services.llm_router import (
    generate_llm_response
)

from app.prompts.planner_prompt import (
    get_planner_prompt
)


def generate_dynamic_outline(topic):

    planner_prompt = (
        get_planner_prompt(topic)
    )

    response = generate_llm_response(
        planner_prompt
    )

    sections = []

    for line in response.split("\n"):

        line = line.strip()

        if line.startswith("Section"):

            sections.append(line)

    return sections