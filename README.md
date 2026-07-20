# 🤖 Multi-Agent Research Assistant

An AI-powered Multi-Agent Research Assistant that autonomously searches the web, extracts relevant information, generates structured research reports, and critiques its own output using multiple AI agents.

Built using **LangChain**, **Groq Llama 3.3**, **Tavily Search API**, **BeautifulSoup**, and **Streamlit**.
## Live - https://multi-agent-researchassi.streamlit.app/
---

## 🚀 Features

- 🔍 AI-powered Web Search using Tavily API
- 🌐 Automatic Web Scraping of Search Results
- 🤖 Multi-Agent Architecture
- 📝 Detailed Research Report Generation
- 📊 AI-Based Report Evaluation & Critique
- ⚡ Fast LLM Inference using Groq
- 🎨 Interactive Streamlit User Interface
- 📚 Source Citation Support

---

## 🏗️ System Architecture

```
                User Query
                     │
                     ▼
             Search Agent
                     │
      (Tavily Web Search API)
                     │
                     ▼
             Reader Agent
        (BeautifulSoup Scraper)
                     │
                     ▼
            Writer Agent (LLM)
        Generates Research Report
                     │
                     ▼
            Critic Agent (LLM)
      Reviews & Scores the Report
                     │
                     ▼
              Final Output
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| LLM Framework | LangChain |
| AI Model | Groq (Llama 3.3 70B) |
| Search API | Tavily |
| Web Scraping | BeautifulSoup |
| HTML Parser | lxml |
| Environment | python-dotenv |

---

## 📂 Project Structure

```
Multi-Agent-Research-Assistant/
│
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Multi-Agent-Research-Assistant.git

cd Multi-Agent-Research-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🤖 Multi-Agent Workflow

### 🔎 Search Agent

- Performs intelligent web search
- Retrieves relevant URLs using Tavily API

---

### 📖 Reader Agent

- Visits selected webpages
- Extracts meaningful content using BeautifulSoup

---

### ✍️ Writer Agent

- Uses Groq Llama 3.3
- Generates a structured research report including:
  - Introduction
  - Key Findings
  - Conclusion
  - References

---

### 🧐 Critic Agent

Evaluates the generated report based on:

- Accuracy
- Completeness
- Clarity
- Structure

Returns:

- Overall Score
- Strengths
- Areas for Improvement
- Final Verdict

---

## 📸 Demo

> Add screenshots of your application here.

Example:

- Home Page
- Generated Research Report
- Critic Evaluation

---

## 💡 Example Topics

- Artificial Intelligence in Healthcare
- Future of Quantum Computing
- Electric Vehicles Market Analysis
- Cybersecurity Trends
- Climate Change Technologies

---

## 🎯 Future Improvements

- PDF Export
- Markdown Download
- Research History
- Multi-language Support
- RAG Integration
- Memory-enabled Agents
- Live Streaming Responses
- Citation Verification

---

## 📈 Learning Outcomes

This project demonstrates practical implementation of:

- Multi-Agent Systems
- Large Language Models (LLMs)
- LangChain Framework
- Prompt Engineering
- Web Search Integration
- AI Report Generation
- Autonomous Agent Collaboration

---

## 👨‍💻 Author

**Priyanshu Singh**

Final Year B.E. Computer Science Engineering  
UIET, Panjab University

LinkedIn: https://www.linkedin.com/in/priyanshu-singh-287b37224/



---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
