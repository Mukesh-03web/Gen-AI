import sys
sys.path.insert(0, ".")

from app.services.document import load_pdf, split_documents
from app.services.vectorstore import create_vectorstore


def main():
    print("Loading PDF...")
    documents = load_pdf()
    print(f"Loaded {len(documents)} pages")

    print("Splitting into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    print("Creating vector store...")
    create_vectorstore(chunks)
    print("Done! Resume is now stored in the vector database.")


if __name__ == "__main__":
    main()
