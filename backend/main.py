# ---------------------------
# FastAPI Backend - SAFE SPACE
# ---------------------------

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from ai_agent import handle_query  # ✅ Correct import

app = FastAPI()


# ---------------------------
# Request Model
# ---------------------------
class Query(BaseModel):
    message: str


# ---------------------------
# API Endpoint
# ---------------------------
@app.post("/ask")
async def ask(query: Query):
    result = handle_query(query.message)
    return result


# ---------------------------
# Run Server
# ---------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)