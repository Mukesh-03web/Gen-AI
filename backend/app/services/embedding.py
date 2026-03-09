from langchain_community.embeddings import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL

embedding_model = None


def get_embedding_model():
    global embedding_model
    if embedding_model is None:
        embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return embedding_model
