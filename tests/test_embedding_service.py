eimport os
from app.embedding_service import load_text_from_file, split_text

def test_load_text():
    text = load_text_from_file("data/example.txt")
    assert isinstance(text, str)
    assert len(text) > 0

def test_split_text():
    chunks = split_text("a" * 1000, chunk_size=200)
    assert len(chunks) == 5
    assert all(isinstance(c, str) for c in chunks)
