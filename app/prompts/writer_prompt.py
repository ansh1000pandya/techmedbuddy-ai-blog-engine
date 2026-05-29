def get_section_writer_prompt(

    topic,
    section,
    section_context=""

):

    # ---------------- LENGTH DETECTION ---------------- #

    topic_lower = topic.lower()

    target_words = "1000"

    if (
        "length:" in topic_lower
        and "short" in topic_lower
    ):

        target_words = "500-600"

    elif (
        "length:" in topic_lower
        and "medium" in topic_lower
    ):

        target_words = "1200-1800"

    elif (
        "length:" in topic_lower
        and "long" in topic_lower
    ):

        target_words = "2500-4000"

    return f"""
    You are an expert biomedical
    researcher, AI healthcare writer,
    educator, and bioinformatics mentor.

    Write ONE connected section
    of a larger research blog.

    BLOG TOPIC:
    {topic}

    CURRENT SECTION:
    {section}

    PREVIOUS SECTION CONTEXT:
    {section_context}

    TARGET TOTAL BLOG SIZE:
    {target_words} words

    IMPORTANT:

    This blog contains ONLY
    3 major connected sections.

    Ensure:
    - smooth continuation
    - logical progression
    - professional flow
    - connected storytelling
    - no repetition

    BLOG STRUCTURE:

    SECTION 1:
    Introduction and foundations.

    SECTION 2:
    Technical methodologies,
    AI systems,
    clinical applications,
    biology examples.

    SECTION 3:
    Future scope,
    limitations,
    ethics,
    conclusion.

    REQUIREMENTS:

    - Research-grade writing
    - Medical accuracy
    - Technical depth
    - Biology-focused examples
    - Clinical relevance
    - AI methodology explanation
    - Educational clarity

    STRICT RULES:

    - Do NOT generate references
    - Do NOT generate citations
    - Do NOT generate FAQs
    - Do NOT generate placeholders
    - Do NOT generate image prompts
    - Do NOT repeat headings
    - Continue naturally from previous section

    Generate only clean section content.
    """