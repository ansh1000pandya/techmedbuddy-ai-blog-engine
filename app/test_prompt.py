from app.prompts.planner_prompt import get_blog_outline_prompt
from app.services.llm_router import generate_llm_response

topic = "AI in Personalized Medicine"

prompt = get_blog_outline_prompt(topic)

response = generate_llm_response(prompt)

print(response)
