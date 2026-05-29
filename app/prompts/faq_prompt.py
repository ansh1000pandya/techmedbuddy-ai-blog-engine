def get_faq_prompt(topic):

    prompt = f"""
You are an expert healthcare educator and AI researcher.

Generate 8 high-quality FAQs with answers
for the following topic.

TOPIC:
{topic}

RULES:
- Questions should sound realistic
- Answers should be concise and informative
- Use scientific but readable language
- Focus on AI + Healthcare + Personalized Medicine
- Avoid repetition
- Use markdown formatting

FORMAT:

## Frequently Asked Questions (FAQs)

### 1. Question?

Answer...

### 2. Question?

Answer...

"""

    return prompt