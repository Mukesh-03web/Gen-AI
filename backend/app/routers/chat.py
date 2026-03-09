from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm import get_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = get_answer(request.question)
    return ChatResponse(answer=answer)
