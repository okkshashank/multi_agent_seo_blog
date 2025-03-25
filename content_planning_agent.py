import json
import os

# Load research data
research_file = "../research_data.json"

if not os.path.exists(research_file):
    print("🚨 No research data found! Run the Research Agent first.")
    exit()

with open(research_file, "r", encoding="utf-8") as file:
    research_data = json.load(file)

# Extract key research points
topic = research_data.get("topic", "HR Trends")
key_points = research_data.get("key_points", [])

# Generate a structured outline based on research
outline = {
    "title": f"{topic}: Key Insights & Future Trends",
    "sections": [
        {"heading": "Introduction", "content": f"Overview of {topic}"},
        *[
            {"heading": key, "content": f"Detailed discussion on {key.lower()}."}
            for key in key_points
        ],
        {"heading": "Conclusion", "content": "Summary and final thoughts."},
    ]
}

# Save the outline to a file
outline_file = "../blog_outline.json"
with open(outline_file, "w", encoding="utf-8") as file:
    json.dump(outline, file, indent=4)

print("✅ Content outline generated successfully!")
