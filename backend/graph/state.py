from typing import TypedDict, List, Dict


class GraphState(TypedDict):
    session_id: str
    message: str
    history: List[Dict]
    response: str
