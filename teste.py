import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=groq_api_key,
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is 2+2?",
        }
    ],
    model="llama3-70b-8192",
)
print(chat_completion.choices[0].message.content)
