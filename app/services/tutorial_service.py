"""
Single-topic tutorial generation service.
"""

from app.services.markdown_cleaner import MarkdownCleaner
from app.services.teaching_style_prompt import (
    TEACHING_STYLE_PROMPT
)

from app.services.groq_service import (
    generate_fast_content
)


class TutorialService:

    def generate_topic(
        self,
        topic_title: str,
        additional_requirements: list = None
    ) -> str:

        if additional_requirements is None:
            additional_requirements = []

        prompt = f"""
{TEACHING_STYLE_PROMPT}

Teach this Python topic naturally.

TOPIC:
{topic_title}

ADDITIONAL REQUIREMENTS:
{additional_requirements}

IMPORTANT:
- Do NOT say:
  "next topic"
  "moving forward"
  "in the next section"

- Teach naturally like a real tutor.

- Include:
  - beginner-friendly explanations
  - Python code examples
  - outputs for code
  - common beginner mistakes
  - quick revision notes

- Use markdown formatting.

- Keep explanations focused ONLY on this topic.
"""

        print("=" * 60)
        print(f"GENERATING TOPIC: {topic_title}")
        print("=" * 60)

        response = generate_fast_content(prompt)

        cleaned_response = MarkdownCleaner.clean(
            response
        )

        return cleaned_response