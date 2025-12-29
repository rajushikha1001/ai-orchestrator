from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_agent

app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "AI Orchestrator API Running"}

@app.post("/query")
def ask_ai(q: Query):
    response = run_agent(q.text)
    return {"response": response}
