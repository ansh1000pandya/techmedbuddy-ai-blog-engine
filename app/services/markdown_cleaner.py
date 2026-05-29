"""
Markdown cleanup utilities.
Improves Streamlit rendering reliability.
"""

import re


class MarkdownCleaner:

    @staticmethod
    def clean(markdown_text: str) -> str:

        text = markdown_text

        # Normalize excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove duplicated headings
        lines = text.split("\n")

        cleaned_lines = []

        previous_line = ""

        for line in lines:

            if (
                line.strip() == previous_line.strip()
                and line.startswith("#")
            ):
                continue

            cleaned_lines.append(line)

            previous_line = line

        text = "\n".join(cleaned_lines)

        # Ensure code blocks are closed
        code_block_count = text.count("```")

        if code_block_count % 2 != 0:
            text += "\n```"

        return text.strip()