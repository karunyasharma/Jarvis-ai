from langgraph.graph import StateGraph, END

from graph.state import GraphState
from agents.manager import manager_node

workflow = StateGraph(GraphState)

workflow.add_node("manager", manager_node)

workflow.set_entry_point("manager")

workflow.add_edge("manager", END)

graph = workflow.compile()