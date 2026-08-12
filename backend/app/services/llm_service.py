from groq import Groq

from backend.app.config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


def generate_llm_response(message: str) -> str:

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are MediBot, a friendly medical AI assistant. "
                    "You can have normal conversations such as greetings, "
                    "introductions, and simple casual questions. "
                    "For casual messages, respond naturally and briefly. "
                    "When discussing medical topics, provide general "
                    "educational information and do not claim to diagnose "
                    "diseases or replace a doctor. "
                    "If a situation may be urgent, advise the user to "
                    "seek appropriate professional medical care."
                ),
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return response.choices[0].message.content