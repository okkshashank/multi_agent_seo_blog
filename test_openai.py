import os
import openai
from dotenv import load_dotenv

# Load API Key
load_dotenv(dotenv_path="C:/Users/shash/multi_agent_seo_blog/.env")
api_key = os.getenv("OPENAI_API_KEY")

# Test OpenAI API
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Test message: Hello, OpenAI!"}],
        api_key=api_key
    )
    print("✅ OpenAI API is working!")
    print("Response:", response["choices"][0]["message"]["content"])
except Exception as e:
    print("❌ OpenAI API Error:", e)
