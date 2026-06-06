from app.services.llm_router import (
    generate_llm_response
)


def extract_concepts(
    section_title,
    section_content
):

    prompt = f"""
You are a curriculum analyzer.

SECTION:
{section_title}

CONTENT:
{section_content}

Extract the important concepts taught.

RULES:

- Return only concepts
- One per line
- Maximum 20 concepts
- No explanations

Example:

variables
assignment
integer
float
string
"""

    response = generate_llm_response(
        prompt
    )

    concepts = []

    for line in response.splitlines():

        line = line.strip()

        if line:

            concepts.append(
                line.lower()
            )

    return concepts