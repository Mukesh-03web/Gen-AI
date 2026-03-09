from langchain_community.vectorstores import Chroma
from app.config import CHROMA_PERSIST_DIR, CHROMA_COLLECTION_NAME
from app.services.embedding import get_embedding_model


def create_vectorstore(chunks):
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory=CHROMA_PERSIST_DIR,
        collection_name=CHROMA_COLLECTION_NAME,
    )
    return vectorstore


def load_vectorstore():
    vectorstore = Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=get_embedding_model(),
        collection_name=CHROMA_COLLECTION_NAME,
    )
    return vectorstore


def search(query, k=3):
    vectorstore = load_vectorstore()
    results = vectorstore.similarity_search(query, k=k)
    return results
