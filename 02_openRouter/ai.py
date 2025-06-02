from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("deepseek/deepseek-chat-v3-0324:free")
)

# Send a chat completion request
response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)

# Print the AI's response
print(response.choices[0].message.content)
