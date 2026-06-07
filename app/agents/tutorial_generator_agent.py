from app.services.llm_router import (
    generate_llm_response
)


class TutorialGeneratorAgent:

    def __init__(self):

        self.generated_sections = []

    # --------------------------------------------------
    # GENERATE SINGLE SECTION
    # --------------------------------------------------

    def generate_section(
        self,
        section_data
    ):

        section_title = (
            section_data["title"]
        )

        section_prompt = (
            section_data["prompt"]
        )

        print("\n" + "=" * 60)
        print(
            f"GENERATING: {section_title}"
        )
        print("=" * 60)

        final_prompt = f"""
{section_prompt}

IMPORTANT:

Write only this section.

Do not generate future sections.

Do not repeat previously generated content.

Format:

# {section_title}

Use proper markdown.
"""

        content = generate_llm_response(
            final_prompt
        )

        self.generated_sections.append(
            section_title
        )

        return content

    # --------------------------------------------------
    # GENERATE COMPLETE TUTORIAL
    # --------------------------------------------------

    def generate_tutorial(
        self,
        tutorial_title,
        selected_sections
    ):

        tutorial_parts = []

        tutorial_parts.append(
            f"# {tutorial_title}"
        )

        for section in selected_sections:

            content = self.generate_section(
                section
            )

            tutorial_parts.append(
                content
            )

        tutorial = "\n\n".join(
            tutorial_parts
        )

        return tutorial