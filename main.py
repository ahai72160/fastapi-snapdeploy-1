from fastapi import FastAPI

app = FastAPI(
    title="Fast Deploy FastAPI API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "FastAPI deployed successfully"
    }


@app.get("/health")
def health():
    return {
        "healthy": True
    }
