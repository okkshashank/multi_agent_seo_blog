import json
import os

# Sample research data (Replace this with actual research function)
research_data = {
    "topic": "Future of Remote Work in HR",
    "key_points": [
        "Rise of hybrid work models",
        "Impact on employee productivity",
        "Challenges in remote hiring",
        "Technology driving remote work trends"
    ]
}

# Save research data to a file
research_file = "../research_data.json"
with open(research_file, "w", encoding="utf-8") as file:
    json.dump(research_data, file, indent=4)

print("✅ Research data saved successfully!")
