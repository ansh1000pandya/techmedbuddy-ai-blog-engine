import re

from app.services.llm_router import (
    generate_llm_response
)

from app.services.reviewer_service import (
    review_section
)

from app.prompts.writer_prompt import (
    get_section_writer_prompt
)

from app.prompts.planner_prompt import (
    get_planner_prompt
)

from app.services.pubmed_service import (
    get_verified_references
)


# ---------------- CLEANING ---------------- #

def clean_section_content(content):

    fake_patterns = [

        r"## References.*",
        r"# References.*",
        r"References.*",

        r"## FAQs.*",
        r"# FAQs.*",
        r"FAQs.*",

        r"\[.*?Insert Image.*?\]",
        r"\[.*?Image.*?\]",

        r"\[\d+\]",

    ]

    for pattern in fake_patterns:

        content = re.sub(
            pattern,
            "",
            content,
            flags=re.DOTALL
        )

    return content.strip()


# ---------------- MAIN BLOG PIPELINE ---------------- #

def generate_blog(topic):

    final_blog = ""

    # ---------------- TITLE ---------------- #

    cleaned_title = topic

    if "Topic:" in topic:

        try:

            cleaned_title = (
                topic.split("Topic:")[1]
                .split("Audience:")[0]
                .strip()
            )

        except:

            cleaned_title = topic

    final_blog += f"# {cleaned_title}\n\n"

    # ---------------- PLANNER AGENT ---------------- #

    print("\nGenerating Dynamic Outline...\n")

    planner_prompt = get_planner_prompt(
        topic
    )

    planner_output = generate_llm_response(
        planner_prompt
    )

    print("\nGenerated Outline:\n")

    print(planner_output)

    # ---------------- SECTION EXTRACTION ---------------- #

    sections = []

    for line in planner_output.split("\n"):

        line = line.strip()

        if line.startswith("Section"):

            sections.append(line)

    # ---------------- FALLBACK ---------------- #

    if len(sections) < 3:

        sections = [

            "Section 1: Introduction",

            "Section 2: Core Concepts and Applications",

            "Section 3: Future Scope and Conclusion"

        ]

    print("\nDetected Sections:\n")

    print(sections)

    # ---------------- CONTINUITY MEMORY ---------------- #

    previous_section_summary = ""

    # ---------------- SECTION GENERATION LOOP ---------------- #

    for section in sections:

        print(
            f"\nGenerating Section: {section}\n"
        )

        MAX_RETRIES = 2

        MIN_SCORE = 6

        approved_content = ""

        for attempt in range(MAX_RETRIES):

            print(
                f"\nAttempt {attempt + 1}\n"
            )

            # ---------------- WRITER PROMPT ---------------- #

            writer_prompt = (
                get_section_writer_prompt(

                    topic,

                    section,

                    previous_section_summary

                )
            )

            generated_content = (
                generate_llm_response(
                    writer_prompt
                )
            )

            generated_content = (
                clean_section_content(
                    generated_content
                )
            )

            # ---------------- REVIEWER ---------------- #

            review = review_section(

                topic,

                section,

                generated_content

            )

            score = review["score"]

            feedback = review["feedback"]

            print(
                f"\nReviewer Score: {score}\n"
            )

            # ---------------- APPROVED ---------------- #

            if score >= MIN_SCORE:

                print(
                    "\nSection Approved\n"
                )

                approved_content = (
                    generated_content
                )

                break

            # ---------------- RETRY ---------------- #

            else:

                print(
                    "\nSection Rejected\n"
                )

                print(
                    f"\nReviewer Feedback:\n{feedback}\n"
                )

                retry_prompt = f"""
                Improve this healthcare
                research section.

                SECTION:
                {section}

                PREVIOUS SECTION:
                {previous_section_summary}

                ORIGINAL CONTENT:
                {generated_content}

                REVIEWER FEEDBACK:
                {feedback}

                Improve:
                - technical depth
                - continuity
                - clarity
                - educational quality
                - medical accuracy
                - topic relevance

                STRICT RULES:
                - no references
                - no citations
                - no FAQs
                - no placeholders
                """

                improved_content = (
                    generate_llm_response(
                        retry_prompt
                    )
                )

                improved_content = (
                    clean_section_content(
                        improved_content
                    )
                )

                second_review = (
                    review_section(

                        topic,

                        section,

                        improved_content

                    )
                )

                second_score = (
                    second_review["score"]
                )

                print(
                    f"\nImproved Score: {second_score}\n"
                )

                if second_score >= MIN_SCORE:

                    print(
                        "\nImproved Version Approved\n"
                    )

                    approved_content = (
                        improved_content
                    )

                    break

                else:

                    approved_content = (
                        improved_content
                    )

        # ---------------- BLOG APPEND ---------------- #

        final_blog += (
            f"\n\n## {section}\n\n"
        )

        final_blog += approved_content

        final_blog += "\n\n"

        # ---------------- CONTEXT MEMORY ---------------- #

        previous_section_summary = (
            approved_content[-1500:]
        )

    # ---------------- VERIFIED REFERENCES ---------------- #

    print(
        "\nFetching Verified References...\n"
    )

    references = (
        get_verified_references(
            cleaned_title,
            max_results=20
        )
    )

    final_blog += "\n\n# References\n\n"

    if len(references) > 0:

        unique_refs = []

        seen = set()

        for ref in references:

            normalized = ref.lower().strip()

            if normalized not in seen:

                unique_refs.append(ref)

                seen.add(normalized)

        for index, ref in enumerate(
            unique_refs,
            start=1
        ):

            final_blog += (
                f"{index}. {ref}\n\n"
            )

    else:

        final_blog += (
            "No verified references found.\n"
        )

    # ---------------- FAQ GENERATION ---------------- #

    print("\nGenerating FAQs...\n")

    faq_prompt = f"""
    Generate 10 educational FAQs
    for this topic:

    {cleaned_title}

    REQUIREMENTS:

    - Question and answer only
    - Professional explanations
    - Educational clarity
    - Biology-friendly explanations
    - No citations
    - No references
    - No markdown tables

    FORMAT:

    Q1:
    A1:

    Q2:
    A2:
    """

    faq_content = generate_llm_response(
        faq_prompt
    )

    # ---------------- CLEAN FAQS ---------------- #

    faq_content = re.sub(

        r"References.*",

        "",

        faq_content,

        flags=re.DOTALL

    )

    faq_content = re.sub(

        r"\[\d+\]",

        "",

        faq_content

    )

    # ---------------- APPEND FAQS ---------------- #

    final_blog += "\n\n# FAQs\n\n"

    final_blog += faq_content

    # ---------------- FINAL CLEAN ---------------- #

    final_blog = re.sub(

        r"\n{3,}",

        "\n\n",

        final_blog

    )

    return final_blog