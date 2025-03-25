import json
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Key
API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded
if not API_KEY:
    print("🚨 OpenAI API key is missing! Please set it in your .env file.")
    exit()

# Load blog outline
outline_file = "../blog_outline.json"

if not os.path.exists(outline_file):
    print("🚨 No outline found! Run the Content Planning Agent first.")
    exit()

with open(outline_file, "r", encoding="utf-8") as file:
    outline = json.load(file)

# Initialize OpenAI client
client = openai.OpenAI(api_key=API_KEY)

# Generate blog content
blog_content = f"## {outline['title']}\n\n"

for section in outline["sections"]:
    prompt = f"Write a detailed section for a blog post about {outline['title']}. Section: {section['heading']}. {section['content']}"
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        generated_text = response.choices[0].message.content
    except Exception as e:
        print(f"🚨 Error generating content for {section['heading']}: {e}")
        continue
    
    blog_content += f"### {section['heading']}\n\n{generated_text}\n\n"

# Save blog post
blog_file = "../generated_blog.md"
with open(blog_file, "w", encoding="utf-8") as file:
    file.write(blog_content)

print("✅ Blog content generated successfully! Check 'generated_blog.md'.")
