from fastapi import APIRouter, Form, HTTPException

from app.services.rag import ask_question

router = APIRouter(tags=["ask"])


@router.post("/ask")
async def ask(question: str = Form(...)):
    try:
        answer = ask_question(question)
    except ConnectionError as exc:
        raise HTTPException(
            status_code=503,
            detail="Modelos indisponíveis. Verifique se o app está rodando na bandeja.",
        ) from exc
    except OSError as exc:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar aos modelos em localhost:11434.",
        ) from exc

    return {"answer": answer}
