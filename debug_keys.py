import os
from dotenv import load_dotenv

# Force load the .env file
load_dotenv()

key = os.getenv("MISTRAL_API_KEY")

if key is None:
    print("❌ FAILED: Python cannot find the .env file or the MISTRAL_API_KEY inside it.")
    print("Make sure the file is named exactly .env (with the dot at the start).")
elif not key.startswith("sk-"):
    print(f"❌ INVALID FORMAT: Your key starts with '{key[:3]}'. It MUST start with 'sk-'.")
else:
    print(f"✅ KEY DETECTED: Your key is loaded and starts with {key[:7]}...")
    print("If you still get 401, the issue is on Mistral's website (Billing/Verification).")