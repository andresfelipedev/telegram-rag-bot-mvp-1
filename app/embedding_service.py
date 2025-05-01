import openai
from chromadb import PersistentClient
from app.config import OPENAI_API_KEY

# Inicializar API Key
openai.api_key = OPENAI_API_KEY

# Cliente ChromaDB actualizado
chroma_client = PersistentClient(path="db")

COLLECTION_NAME = "documentos"

def load_text_from_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def split_text(text: str, chunk_size: int = 300) -> list:
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def embed_text_chunks(chunks: list[str]) -> list[list[float]]:
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=chunks
    )
    return [item.embedding for item in response.data]

def ingest_document(filepath: str):
    text = load_text_from_file(filepath)
    chunks = split_text(text)
    embeddings = embed_text_chunks(chunks)

    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)
    ids = [f"chunk-{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    return len(chunks)

