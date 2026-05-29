from app.services.groq_service import generate_fast_content


def generate_llm_response(prompt):

    try:
        return generate_fast_content(prompt)

    except Exception as e:

        return f"LLM Error: {str(e)}"