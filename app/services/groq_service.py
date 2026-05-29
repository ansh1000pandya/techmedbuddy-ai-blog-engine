import time

from groq import Groq
from groq import RateLimitError

from app.config.settings import (
    GROQ_API_KEY,
    GROQ_MODEL
)

client = Groq(api_key=GROQ_API_KEY)


def generate_fast_content(prompt: str):

    attempts = 3

    for attempt in range(attempts):

        try:

            completion = client.chat.completions.create(

                model=GROQ_MODEL,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.7,

                max_tokens=1200
            )

            return completion.choices[0].message.content

        except RateLimitError:

            print("=" * 60)
            print("GROQ RATE LIMIT REACHED")
            print(f"Retry Attempt: {attempt + 1}")
            print("=" * 60)

            time.sleep(3)

        except Exception as e:

            print("=" * 60)
            print("GROQ GENERATION ERROR")
            print(str(e))
            print("=" * 60)

            return (
                "An error occurred while generating content."
            )

    return (
        "Rate limit exceeded. "
        "Please wait a few seconds and try again."
    )