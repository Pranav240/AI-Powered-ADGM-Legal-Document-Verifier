import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not found")
else:
    print("✅ Key loaded:", api_key[:6] + "..." + api_key[-4:])

    # Optional: small test call
    client = genai.Client(api_key=api_key)
    res = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Say hello in 5 words"
    )
    print("Gemini says:", res.text)
