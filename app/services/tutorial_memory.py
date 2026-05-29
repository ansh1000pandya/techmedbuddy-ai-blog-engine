"""
Tutorial memory manager.
Tracks continuity and reduces repetition.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class TutorialMemory:

    covered_topics: List[str] = field(default_factory=list)

    used_examples: List[str] = field(default_factory=list)

    defined_terms: List[str] = field(default_factory=list)

    generated_sections: List[str] = field(default_factory=list)

    # ---------------------------------------------------------
    # TOPIC MEMORY
    # ---------------------------------------------------------

    def add_topic(self, topic: str):

        if topic and topic not in self.covered_topics:

            self.covered_topics.append(topic)

    # ---------------------------------------------------------
    # EXAMPLE MEMORY
    # ---------------------------------------------------------

    def add_example(self, example: str):

        if example and example not in self.used_examples:

            self.used_examples.append(example)

    # ---------------------------------------------------------
    # TERM MEMORY
    # ---------------------------------------------------------

    def add_term(self, term: str):

        if term and term not in self.defined_terms:

            self.defined_terms.append(term)

    # ---------------------------------------------------------
    # SECTION MEMORY
    # ---------------------------------------------------------

    def add_section(self, section: str):

        if section:

            self.generated_sections.append(section)

    # ---------------------------------------------------------
    # CONTEXT BUILDER
    # ---------------------------------------------------------

    def build_memory_context(self) -> str:

        recent_topics = self.covered_topics[-3:]

        if not recent_topics:

            return ""

        return (
            "Recently Covered Topics:\n- "
            + "\n- ".join(recent_topics)
        )