def get_tutorial_prompt(

    tutorial_topic,
    difficulty_level,
    target_audience

):

    return f"""
    You are an expert biomedical educator,
    AI researcher, bioinformatician,
    and programming mentor.

    Create a COMPLETE educational tutorial.

    TOPIC:
    {tutorial_topic}

    DIFFICULTY LEVEL:
    {difficulty_level}

    TARGET AUDIENCE:
    {target_audience}

    REQUIREMENTS:

    1. Beginner-friendly explanation
    2. Technical explanation
    3. Real-world clinical examples
    4. Biology-focused examples
    5. Bioinformatics applications
    6. Step-by-step explanation
    7. Python code examples if relevant
    8. Research applications
    9. Student-friendly teaching style
    10. Real stories or case studies

    STRUCTURE:

    # Introduction

    # Why This Matters in Biology/Healthcare

    # Core Concept Explanation

    # Clinical Example

    # Bioinformatics Example

    # Python Implementation

    # Step-by-Step Breakdown

    # Common Mistakes

    # Real Research Applications

    # Practice Exercises

    # FAQs

    STRICT RULES:

    - NO references
    - NO citations
    - NO markdown tables
    - NO placeholders
    - NO image prompts

    Make tutorial highly engaging and educational.
    """