import json
from app.services.llm_router import (
    generate_llm_response
)


def generate_dynamic_outline(topic: str):

    prompt = f"""
You are an expert curriculum designer.

Create a tutorial outline.

TOPIC:
{topic}

Return ONLY valid JSON.

Example:

[
    "Introduction",
    "What is BLAST",
    "Sequence Similarity",
    "BLAST Algorithm",
    "BLAST Databases",
    "Interpreting Results",
    "Applications",
    "Best Practices",
    "Summary"
]

Do not return explanations.
Do not return markdown.
Do not return headings.
Do not return anything except JSON.
"""


    response = generate_llm_response(
        prompt
    )

    try:
        sections = json.loads(response)
        if isinstance(sections, list):
            unique_sections = []
            for section in sections:
                section = str(section).strip()
                if (
                    section
                    and section not in unique_sections
                ):
                    unique_sections.append(
                        section
                    )
            print("\nPLANNER OUTPUT:")
            print(unique_sections)
            return unique_sections
    except Exception as e:
        print(f"Planner JSON Parse Error: {e}")
        return []


    
        
        