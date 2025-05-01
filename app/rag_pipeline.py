import openai
from app.config import OPENAI_API_KEY
from app.retriever import retrieve_relevant_chunks

openai.api_key = OPENAI_API_KEY

def build_prompt(context_chunks: list[str], user_question: str) -> str:
    context = "\n---\n".join(context_chunks)
    prompt = (
        f"Contexto relevante sobre Miky’s Pasta Bga:\n{context}\n\n"
        f"Pregunta del usuario:\n{user_question}\n\n"
        "Responde de forma clara y precisa SOLO usando el contexto proporcionado. "
        "Si no hay suficiente información, responde que no lo sabes."
    )
    return prompt

def generate_answer(user_question: str) -> str:
    context_chunks = retrieve_relevant_chunks(user_question)
    
    if not context_chunks:
        return "Lo siento, no tengo suficiente información para responder esa pregunta."

    prompt = build_prompt(context_chunks, user_question)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Actúas como el asistente oficial de Miky’s Pasta Bga, una barra de pasta artesana en Bucaramanga. "
                    "Tu trabajo es responder preguntas de los clientes usando solo el contexto provisto. "
                    "Si no sabes algo, es mejor decirlo que inventar."
                )
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # Más precisión, menos alucinación
    )

    return response.choices[0].message.content.strip()
