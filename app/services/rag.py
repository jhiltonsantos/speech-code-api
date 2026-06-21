from app.dependencies import get_retrieval_chain


def ask_question(question: str) -> str:
    chain = get_retrieval_chain()
    result = chain.invoke({"input": question})
    return result["answer"]
