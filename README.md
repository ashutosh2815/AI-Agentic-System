# 🔎 Dual-Agent AI Deep Research System

This is a dual-agent AI system that performs deep online research using Tavily and generates human-like answers using LangGraph and LangChain.

## 📦 Features

- Research Agent: Uses Tavily for live web search
- Writer Agent: Summarizes and composes professional answers
- LangGraph: Manages agent workflow as a state graph

## 🚀 How to Run

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your GROQ_API_KEY key to `.env`
4. Run the app: `python main.py`

## 📁 Structure

- `agents/`: Agents' logic
- `workflow/`: LangGraph state logic
- `main.py`: Entry point

## 🔧 Future Ideas

- Add third agent for fact-checking
- Integrate with Streamlit for UI


