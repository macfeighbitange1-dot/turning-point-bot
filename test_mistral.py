import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

try:
    response = client.chat.complete(
        model="mistral-tiny",
        messages=[{"role": "user", "content": "Say hello!"}]
    )
    print("✅ SUCCESS! Mistral says:", response.choices[0].message.content)
except Exception as e:
    print("❌ STILL FAILING. Error:", e)