import json

from app.services.llm_router import (
    generate_llm_response
)


def generate_tutorial_plan(topic):

    planner_prompt = f"""
You are an expert curriculum designer.

Create a complete tutorial plan.

TOPIC:
{topic}

For EACH section generate:

1. section title
2. content-generation prompt

Return ONLY valid JSON.

Format:

[
    {{
        "section": "Introduction",
        "prompt": "Teach beginners what BLAST is..."
    }},
    {{
        "section": "BLAST Algorithm",
        "prompt": "Explain how BLAST searches databases..."
    }}
]

Rules:

- 8 to 15 sections
- Beginner to Advanced
- No duplicate sections
- No markdown
- No explanations

Return JSON only.
"""

    response = generate_llm_response(
        planner_prompt
    )

    try:

        tutorial_plan = json.loads(
            response
        )

        return tutorial_plan

    except Exception as e:

        print(
            f"Planner Error: {e}"
        )

        return []