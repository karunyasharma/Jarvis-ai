from fastapi import FastAPI
from api.chat import router as chat_router

app = FastAPI(
    title="Jarvis AI",
    version="1.0.0",
)

app.include_router(chat_router)


@app.get("/")
async def root():
    return {
        "message": "Jarvis AI is running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
