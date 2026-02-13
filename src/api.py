from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import Runner
from src.agent import build_agent

app = FastAPI()

# ✅ LIBERAR CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir só pro seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = build_agent()

# Memória simples por sessão (em RAM)
sessions = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


@app.post("/chat")
async def chat(req: ChatRequest):
    session_id = req.session_id or "default"

    if session_id not in sessions:
        sessions[session_id] = []

    history = sessions[session_id]

    history.append({"role": "user", "content": req.message})

    result = await Runner.run(agent, history)

    reply = result.final_output

    history.append({"role": "assistant", "content": reply})

    return {
        "response": reply,
        "session_id": session_id
    }
