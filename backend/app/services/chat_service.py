from backend.app.services.llm_service import generate_llm_response


def generate_response(message: str) -> str:
    return generate_llm_response(message)