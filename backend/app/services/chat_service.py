from backend.app.services.llm_service import generate_llm_response
from backend.app.services.retrieval_service import retrieve_relevant_chunks


def is_casual_message(message: str) -> bool:

    casual_messages = {
        "hi",
        "hello",
        "hey",
        "hy",
        "hii",
        "hiii",
        "good morning",
        "good afternoon",
        "good evening",
        "how are you",
        "who are you",
        "what are you",
        "thanks",
        "thank you",
        "bye",
        "goodbye",
    }

    return message.strip().lower() in casual_messages


def generate_response(message: str) -> dict:

    # Normal conversation
    if is_casual_message(message):

        answer = generate_llm_response(message)

        return {
            "answer": answer,
            "sources": [],
        }

    # Medical question → RAG
    chunks = retrieve_relevant_chunks(
        query=message,
        top_k=3,
    )

    context = "\n\n".join(
        chunk["text"]
        for chunk in chunks
    )

    prompt = f"""
Use the following medical knowledge context to answer the user's question.

MEDICAL KNOWLEDGE CONTEXT:
{context}

USER QUESTION:
{message}

Instructions:
- Answer using the provided context.
- If the context does not contain enough information, clearly say that the available knowledge base does not contain enough information.
- Do not invent medical facts.
- Provide general educational information only.
- Do not diagnose the user or replace a healthcare professional.
"""

    answer = generate_llm_response(prompt)

    sources = [
        {
            "source": chunk["source"],
            "page": chunk["page"],
        }
        for chunk in chunks
    ]

    return {
        "answer": answer,
        "sources": sources,
    }