from app.retriever import retrieve_relevant_chunks

def test_retrieve_chunks():
    results = retrieve_relevant_chunks("¿De qué trata el documento?")
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(r, str) for r in results)
