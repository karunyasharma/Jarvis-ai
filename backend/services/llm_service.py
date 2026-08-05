from langchain_groq import ChatGroq
from core.settings import settings

llm = ChatGroq(
    model=settings.MODEL_NAME,
    api_key=settings.GROQ_API_KEY,
    temperature=0.3,
)

def chat_with_jarvis(message: str) -> str:
    response = llm.invoke(message)
    return response.content