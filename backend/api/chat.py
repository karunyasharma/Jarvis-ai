from fastapi import APIRouter
from pydantic import BaseModel
from graph.workflow import graph

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "session_id": request.session_id,
            "message": request.message,
            "history": [],
            "response": "",
        }
    )

    return {
        "user": request.message,
        "assistant": result["response"],
        "history": result["history"],
    }