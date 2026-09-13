import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API key loaded:", bool(api_key))

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain in one sentence why a very large financial transaction may be suspicious."
        }
    ]
)

print("\nGroq Response:")
print(response.choices[0].message.content)