from app.rag_pipeline import generate_answer

def test_generate_answer():
    question = "¿De qué trata el documento de ejemplo?"
    response = generate_answer(question)
    assert isinstance(response, str)
    assert len(response) > 0
