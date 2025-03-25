import json
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Key
API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded
if not API_KEY:
    print("🚨 OpenAI API key is missing! Please set it in your .env file.")
    exit()

# Load generated blog post
blog_file = "../generated_blog.md"

if not os.path.exists(blog_file):
    print("🚨 No blog content found! Run the Content Generation Agent first.")
    exit()

with open(blog_file, "r", encoding="utf-8") as file:
    blog_content = file.read()

# Define SEO optimization prompt
seo_prompt = f"""
Improve the following blog post for SEO. Ensure:
1. Proper keyword usage
2. Meta descriptions and title tag optimization
3. Readability improvements
4. Headings and subheadings are properly structured
5. Internal linking recommendations (if applicable)

Blog Post:
{blog_content}
"""

# Initialize OpenAI client
client = openai.OpenAI(api_key=API_KEY)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": seo_prompt}]
    )
    optimized_content = response.choices[0].message.content
except Exception as e:
    print(f"🚨 Error optimizing content: {e}")
    exit()

# Save optimized blog post
optimized_blog_file = "../optimized_blog.md"
with open(optimized_blog_file, "w", encoding="utf-8") as file:
    file.write(optimized_content)

print("✅ Blog optimized for SEO successfully! Check 'optimized_blog.md'.")
