import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openai/gpt-4o-mini"


def explain_code(code):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
You are an expert programming tutor.

Explain the following code in very simple English.

Include:
1. Purpose
2. Variables
3. Functions
4. Logic
5. Output

Code:

{code}
"""

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)

        print(response.status_code)
        print(response.text)

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return str(e)


