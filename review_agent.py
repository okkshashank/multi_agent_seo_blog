import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("🚨 OpenAI API Key not found! Please check your .env file.")

openai.api_key = api_key

# Load the optimized blog content
input_file = "output/optimized_blog.md"
output_file = "output/final_reviewed_blog.md"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        blog_content = file.read()
except FileNotFoundError:
    print("🚨 Optimized blog not found! Run the SEO Optimization Agent first.")
    exit()

# Review and improve content
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Make sure you're using an available model
    messages=[
        {"role": "system", "content": "You are a professional editor. Improve the blog for clarity, grammar, and readability."},
        {"role": "user", "content": f"Review and improve this blog:\n\n{blog_content}"}
    ]
)

# Extract reviewed content
reviewed_content = response["choices"][0]["message"]["content"]

# Save the reviewed content
with open(output_file, "w", encoding="utf-8") as file:
    file.write(reviewed_content)

print(f"✅ Blog reviewed and saved to {output_file}")
