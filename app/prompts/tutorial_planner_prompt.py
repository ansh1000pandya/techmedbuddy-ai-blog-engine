def get_tutorial_planner_prompt(topic):

    return f"""
    You are an expert biomedical
    educator and curriculum architect.

    Analyze this tutorial topic:

    TOPIC:
    {topic}

    Generate EXACTLY 3
    topic-specific tutorial sections.

    REQUIREMENTS:

    - Adapt to topic domain
    - Avoid generic structure
    - Ensure educational progression
    - Ensure beginner-to-advanced flow
    - Include biology/clinical/programming relevance
    - Make sections highly topic-specific

    OUTPUT FORMAT:

    Section 1: ...

    Section 2: ...

    Section 3: ...

    ONLY generate section titles.
    """