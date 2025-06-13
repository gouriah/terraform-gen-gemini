import os
import requests
import json

def call_gemini(user_prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Test call
if __name__ == "__main__":
    prompt = "Explain how AI works in a few words"
    result = call_gemini(prompt)
    print(json.dumps(result, indent=2))
