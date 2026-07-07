from fastapi import FastAPI

app = FastAPI(
    title="ReleaseForge API",
    description="Enterprise Artifact & Release Management Platform",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "project": "ReleaseForge",
        "message": "Welcome to ReleaseForge 🚀",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }