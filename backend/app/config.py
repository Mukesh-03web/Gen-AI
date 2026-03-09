import os
from dotenv import load_dotenv

load_dotenv()

# Groq settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# Embedding settings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# ChromaDB settings
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "vectordb")
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "resume")

# Document settings
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))

# Path to resume
RESUME_PATH = os.getenv("RESUME_PATH", "data/Mukesh Updated cv .pdf")
