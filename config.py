from http import client
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/shash/multi_agent_seo_blog/.env")

print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))
