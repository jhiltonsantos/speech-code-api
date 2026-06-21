from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

OLLAMA_BASE_URL = "http://localhost:11434"
LLM_MODEL = "llama3"
EMBED_MODEL = "nomic-embed-text"

CHROMA_DIR = BASE_DIR / "chroma_data"
TMP_UPLOAD_DIR = BASE_DIR / "tmp_uploads"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
RETRIEVER_K = 4

CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
