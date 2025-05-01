import openai
from chromadb import PersistentClient
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

chroma_client = PersistentClient(path="db")
COLLECTION_NAME = "documentos"
TOP_K = 3  # Puedes ajustar según necesidad

def get_embedding(text: str) -> list[float]:
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=[text]
    )
    return response.data[0].embedding

def retrieve_relevant_chunks(query: str, top_k: int = TOP_K) -> list[str]:
    embedding = get_embedding(query)
    collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        include=["documents"]
    )

    documents = results.get("documents", [[]])[0]
    if not documents:
        print("⚠️ No se encontraron fragmentos relevantes para la consulta.")
    else:
        print(f"📚 Fragmentos recuperados ({len(documents)}):\n")
        for i, doc in enumerate(documents, 1):
            print(f"[{i}] {doc}\n")

    return documents
