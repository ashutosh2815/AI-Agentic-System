# research_agent.py
from langchain.agents import initialize_agent, Tool
from langchain_community.tools.tavily_search.tool import TavilySearchResults
from utils.llm_config import load_llm

def get_research_agent():
    search = TavilySearchResults()
    tools = [Tool(name="web-search", func=search.run, description="Search the web for relevant info")]

    llm = load_llm()

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent_type="zero-shot-react-description",
        verbose=True
    )
