from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.post("/review")
def review():
    return {"todo": True}