import json

from app.services.llm_router import (
    generate_llm_response
)


def generate_tutorial_plan(
    topic: str
):

    planner_prompt = f"""
You are a senior curriculum architect.

Your task is to design a complete tutorial plan.

TOPIC:
{topic}

IMPORTANT:

You must create:

1. Tutorial title
2. 8-15 logical sections
3. A detailed generation prompt for EACH section

The prompts should:

- teach ONLY that section
- avoid repeating previous sections
- be beginner friendly
- include examples when appropriate
- include code only if the topic requires code

Return ONLY valid JSON.

Format:

{{
    "tutorial_title": "...",
    "sections": [
        {{
            "id": 1,
            "title": "...",
            "prompt": "..."
        }}
    ]
}}

Do not return markdown.

Do not return explanations.

Return ONLY JSON.
"""

    response = generate_llm_response(
        planner_prompt
    )

    try:

        plan = json.loads(
            response
        )

        print("\n" + "=" * 60)
        print("PLANNER OUTPUT")
        print("=" * 60)

        print(
            json.dumps(
                plan,
                indent=4
            )
        )

        return plan

    except Exception as e:

        print(
            f"Planner Parse Error: {e}"
        )

        print(
            "Raw Response:\n",
            response
        )

        return None