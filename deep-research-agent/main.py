from workflow.graph_workflow import build_graph

if __name__ == "__main__":
    query = input("Enter your research query: ")
    graph_app = build_graph()
    result = graph_app.invoke({"input": query})
    print("\n--- Final Output ---\n")
    print(result["final_output"])
