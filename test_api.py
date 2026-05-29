from app.services.llm_router import generate_llm_response

prompt = "Explain AI in personalized medicine."

response = generate_llm_response(prompt)

print(response)