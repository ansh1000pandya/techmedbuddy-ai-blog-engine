"""
Intent parser for adaptive tutorial generation.
"""


class IntentParser:
    """
    Extracts lightweight educational intent from user prompts.
    """

    BEGINNER_KEYWORDS = [
        "beginner",
        "basic",
        "simple",
        "easy",
        "start",
        "from scratch"
    ]

    ADVANCED_KEYWORDS = [
        "advanced",
        "deep",
        "expert",
        "internals",
        "architecture"
    ]

    def parse(self, user_prompt: str) -> dict:

        prompt_lower = user_prompt.lower()

        difficulty = "intermediate"

        if any(word in prompt_lower for word in self.BEGINNER_KEYWORDS):
            difficulty = "beginner"

        elif any(word in prompt_lower for word in self.ADVANCED_KEYWORDS):
            difficulty = "advanced"

        wants_code = any(
            keyword in prompt_lower
            for keyword in [
                "code",
                "example",
                "python",
                "implement"
            ]
        )

        wants_examples = any(
            keyword in prompt_lower
            for keyword in [
                "example",
                "examples",
                "demo"
            ]
        )

        return {
            "topic": user_prompt.strip(),
            "difficulty": difficulty,
            "wants_code": wants_code,
            "wants_examples": wants_examples,
            "strict_focus": True,
            "style": "conversational"
        }