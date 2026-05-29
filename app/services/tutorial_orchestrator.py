"""
Tutorial orchestration engine.
Handles:
- curriculum extraction
- topic sequencing
- tutorial assembly
- quiz generation
- mini project generation
- HTML export
"""

import os
import re

from markdown import markdown

from app.services.tutorial_service import (
    TutorialService
)

from app.services.markdown_cleaner import (
    MarkdownCleaner
)

from app.services.groq_service import (
    generate_fast_content
)


class TutorialOrchestrator:

    def __init__(self):

        self.tutorial_service = TutorialService()

    # ---------------------------------------------------------
    # CURRICULUM EXTRACTION
    # ---------------------------------------------------------

    def extract_curriculum(
        self,
        user_prompt: str
    ) -> dict:

        lines = [
            line.strip()
            for line in user_prompt.splitlines()
            if line.strip()
        ]

        topics = []

        requirements = []

        inside_requirements = False

        for line in lines:

            if (
                "additional requirements"
                in line.lower()
            ):
                inside_requirements = True
                continue

            cleaned_line = line.replace("-", "").strip()

            if inside_requirements:
                requirements.append(cleaned_line)

            else:
                topics.append(cleaned_line)

        return {
            "topics": topics,
            "requirements": requirements
        }

    # ---------------------------------------------------------
    # QUIZ GENERATION
    # ---------------------------------------------------------

    def generate_final_quiz(
        self,
        tutorial_topics: list
    ) -> str:

        joined_topics = ", ".join(tutorial_topics)

        prompt = f"""
Create a beginner-friendly Python quiz.

Topics:
{joined_topics}

Include:
- MCQs
- output prediction
- debugging questions
- coding questions

Use markdown formatting.
"""

        return generate_fast_content(prompt)

    # ---------------------------------------------------------
    # MINI PROJECT
    # ---------------------------------------------------------

    def generate_mini_project(
        self,
        tutorial_topics: list
    ) -> str:

        joined_topics = ", ".join(tutorial_topics)

        prompt = f"""
Create a beginner-friendly Python mini project.

Topics:
{joined_topics}

Requirements:
- use variables
- input()
- strings
- operators
- debugging concepts

Include:
- explanation
- full code
- output
"""

        return generate_fast_content(prompt)

    # ---------------------------------------------------------
    # HTML EXPORT
    # ---------------------------------------------------------

    def export_html(
        self,
        markdown_content: str,
        output_name: str = "tutorial_output.html"
    ) -> str:

        html_body = markdown(markdown_content)

        final_html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>TechMedBuddy Tutorial</title>

<style>

body {{
    font-family: Arial, sans-serif;
    line-height: 1.8;
    padding: 40px;
    max-width: 1000px;
    margin: auto;
    background-color: #ffffff;
    color: #222222;
}}

pre {{
    background-color: #f4f4f4;
    padding: 15px;
    overflow-x: auto;
    border-radius: 8px;
}}

code {{
    font-family: Consolas, monospace;
}}

h1, h2, h3 {{
    color: #0d47a1;
}}

</style>

</head>

<body>

{html_body}

</body>

</html>
"""

        output_path = os.path.join(
            os.getcwd(),
            output_name
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(final_html)

        return output_path

    # ---------------------------------------------------------
    # MAIN PIPELINE
    # ---------------------------------------------------------

    def generate_tutorial(
        self,
        user_prompt: str
    ) -> tuple:

        curriculum = self.extract_curriculum(
            user_prompt
        )

        tutorial_parts = []

        tutorial_parts.append(
            "# Complete Python Tutorial"
        )

        # -------------------------------------------------
        # TOPIC GENERATION
        # -------------------------------------------------

        for topic in curriculum["topics"]:

            topic_content = (
                self.tutorial_service.generate_topic(
                    topic_title=topic,
                    additional_requirements=(
                        curriculum["requirements"]
                    )
                )
            )

            tutorial_parts.append(topic_content)

        # -------------------------------------------------
        # QUIZ
        # -------------------------------------------------

        tutorial_parts.append("\n# Final Quiz\n")

        tutorial_parts.append(
            self.generate_final_quiz(
                curriculum["topics"]
            )
        )

        # -------------------------------------------------
        # MINI PROJECT
        # -------------------------------------------------

        tutorial_parts.append("\n# Mini Project\n")

        tutorial_parts.append(
            self.generate_mini_project(
                curriculum["topics"]
            )
        )

        full_tutorial = "\n\n".join(
            tutorial_parts
        )

        cleaned_tutorial = (
            MarkdownCleaner.clean(
                full_tutorial
            )
        )

        html_path = self.export_html(
            cleaned_tutorial
        )

        return (
            cleaned_tutorial,
            html_path
        )


# ---------------------------------------------------------
# STREAMLIT COMPATIBILITY
# ---------------------------------------------------------

def generate_tutorial(user_prompt: str):

    orchestrator = TutorialOrchestrator()

    return orchestrator.generate_tutorial(
        user_prompt
    )