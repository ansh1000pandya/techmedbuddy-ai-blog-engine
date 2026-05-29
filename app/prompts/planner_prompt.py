def get_planner_prompt(topic):

    return f"""
    You are an expert biomedical
    curriculum architect and
    research content planner.

    Analyze this topic carefully:

    TOPIC:
    {topic}

    Your task:

    Generate EXACTLY 3 highly relevant,
    connected blog sections.

    REQUIREMENTS:

    - Sections must match topic domain
    - Avoid generic structures
    - Ensure logical progression
    - Ensure educational flow
    - Adapt to technical topic type
    - Adapt to biology/programming/AI topics
    - Keep section titles concise
    - Sections should feel connected

    OUTPUT FORMAT:

    Section 1: ...
    Section 2: ...
    Section 3: ...

    ONLY generate section titles.
    """