from mistralai import Mistral

# PASTE YOUR KEY INSIDE THE QUOTES BELOW
key = "sk-Fm0AVQRtuTewS48v8bNYk902cpcJBuZA" 

client = Mistral(api_key=key)

try:
    print("Testing connection...")
    response = client.chat.complete(
        model="mistral-small-latest", # Using a more reliable model name
        messages=[{"role": "user", "content": "Is this working?"}]
    )
    print("✅ SUCCESS! Mistral replied:", response.choices[0].message.content)
except Exception as e:
    print("❌ STILL 401. This means Mistral has NOT activated your key yet.")
    print(f"Error Details: {e}")