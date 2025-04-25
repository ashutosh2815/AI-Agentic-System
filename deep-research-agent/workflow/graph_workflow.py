from langgraph.graph import StateGraph
from agents.researcher_agent import get_research_agent
from agents.writer_agent import get_writer_agent
from typing import Annotated

research_agent = get_research_agent()
writer_agent = get_writer_agent()

def research_node(state):
    query = state["input"]
    research_result = research_agent.invoke(query)  # Replaced run() with invoke()
    return {"research_data": research_result}

def draft_node(state):
    notes = state["research_data"]
    answer = writer_agent.invoke(f"Write a detailed answer using:\\n\\n{notes}")  # Replaced run() with invoke()
    return {"final_output": answer}


def build_graph():
    # Define the state schema using Annotated for more control over type and reducers
    state_schema = (
        ("input", str),
        ("research_data", Annotated[str, "reducer"]),  # Example using a reducer
        ("final_output", str)
    )

    # Create the graph with the state schema
    graph = StateGraph(state_schema=state_schema)
    
    graph.add_node("research", research_node)
    graph.add_node("draft", draft_node)

    graph.set_entry_point("research")
    graph.add_edge("research", "draft")
    graph.set_finish_point("draft")

    return graph.compile()

