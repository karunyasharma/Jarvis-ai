from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import chat_with_jarvis

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    reply = chat_with_jarvis(request.message)

    return {
        "user": request.message,
        "assistant": reply
    }