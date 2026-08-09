from fastapi import FastAPI
from api.chat import router as chat_router
from database.db import Base, engine

app = FastAPI(
    title="Jarvis AI",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(chat_router)


@app.get("/")
async def root():
    return {"message": "Jarvis AI is running 🚀"}


@app.get("/health")
async def health():
    return {"status": "healthy"}