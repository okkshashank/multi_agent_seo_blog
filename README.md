 # 🧠 Multi-Agent SEO Blog Generator

A modular multi-agent system for generating SEO-optimized blog articles using autonomous agents powered by LLMs (e.g., OpenAI GPT). Each agent performs a specific task—planning, researching, writing, optimizing, and reviewing—creating a full content pipeline from concept to publish-ready blog.

---

## 🚀 Features

- 📝 **Content Planning Agent**: Generates blog titles, outlines, and key talking points.
- 🔍 **Research Agents**: Gathers factual, relevant, and recent information for each section.
- ✍️ **Content Generation Agent**: Writes coherent, structured blog content based on planning and research.
- 📈 **SEO Optimization Agent**: Enhances the content with SEO strategies (keywords, meta descriptions, etc.).
- ✅ **Review Agent**: Finalizes the article with grammar correction and quality checks.

---

## 🛠️ Setup

### 1. Clone the Repository
git clone https://github.com/yourusername/multi_agent_seo_blog.git
cd multi_agent_seo_blog

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Configure Environment Variables
Configure Environment Variables: OPENAI_API_KEY=your_openai_key_here

---

## ⚙️ How to Run

Use the main script to run the end-to-end pipeline:
python main.py

---

## 📁 Project Structure

multi_agent_seo_blog/
├── agents/
│   ├── content_planning_agent.py
│   ├── research_agents.py
│   ├── content_generation_agent.py
│   ├── seo_optimization_agent.py
│   └── review_agent.py
├── config.py
├── main.py
├── requirements.txt
├── .env
├── test_openai.py
└── README.md

---

## 🧪 Testing

Run a quick test to verify your OpenAI setup:
python test_openai.py

---

## 📌 Future Improvements

🖼️ Add image generation for blog illustrations
🌍 Support multilingual blog generation
📤 One-click publishing to WordPress or Medium
🤖 Integration with CrewAI or AutoGen for dynamic agent coordination

---

##📝 License

MIT License

---
