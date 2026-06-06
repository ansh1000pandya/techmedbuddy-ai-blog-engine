"""
Single-topic tutorial generation service.
"""

from app.services.markdown_cleaner import (
    MarkdownCleaner
)

from app.services.teaching_style_prompt import (
    TEACHING_STYLE_PROMPT
)

from app.services.groq_service import (
    generate_fast_content
)


class TutorialService:

    def generate_topic(
        self,
        topic_title,
        tutorial_mode,
        main_topic,
        memory
    ):

        completed_sections = (
            memory.get_completed_sections()
        )
        
        completed_text = "\n".join(
            [
                f"- {section}"
                for section in completed_sections
            ]
        )
        completed_concepts = (memory.get_concepts())
        concept_text = "\n".join(
            [f"- {concept}"
            for concept in completed_concepts
        ])

        # ---------------------------------
        # THEORY ONLY MODE
        # ---------------------------------

        if tutorial_mode == "Theory Only":

            mode_instruction = """
Generate ONLY theoretical content.

DO NOT include:

- code
- code blocks
- programming exercises
- implementation examples
- output examples

Focus only on explanation,
concepts,
real-world understanding,
and intuition.
"""

        # ---------------------------------
        # THEORY + CODE MODE
        # ---------------------------------

        else:

            mode_instruction = """
Generate both theory and code.

Include:

- explanations
- examples
- code blocks
- output examples
- beginner mistakes
"""

        # ---------------------------------
        # FINAL PROMPT
        # ---------------------------------

        prompt = f"""
{TEACHING_STYLE_PROMPT}

MAIN TOPIC:
{main_topic}

CURRENT SECTION:
{topic_title}

SECTIONS ALREADY COVERED:

{completed_text}

IMPORTANT:

Do NOT repeat concepts from
previous sections.

Do NOT re-explain concepts that already appear in
the CONCEPTS ALREADY TAUGHT list.
Assume the learner already understands:
{concept_text}


Focus ONLY on:

{topic_title}

{mode_instruction}

FORMAT:

# {topic_title}

## Introduction

## Core Concepts

## Examples

#Prompts futher instructions 
## Common Mistakes

## Summary
"""

        # ---------------------------------
        # STORE PROMPT
        # ---------------------------------

        memory.add_prompt(
            section=topic_title,
            prompt=prompt
        )

        print("\n" + "=" * 60)
        print(
            f"GENERATING SECTION: {topic_title}"
        )
        print("=" * 60)

        response = generate_fast_content(
            prompt
        )

        cleaned_response = (
            MarkdownCleaner.clean(
                response
            )
        )

        return cleaned_response