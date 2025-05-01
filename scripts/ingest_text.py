import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



from app.embedding_service import ingest_document

if __name__ == "__main__":
    filepath = "data/mikys_pasta_contexto.txt"
    cantidad = ingest_document(filepath)
    print(f"✅ Se procesaron {cantidad} fragmentos del documento.")
