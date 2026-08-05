from fastapi import FastAPI

app = FastAPI(
    title="Jarvis AI",
    version="1.0.0",
    description="AI Executive Personal Assistant"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Jarvis AI 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }