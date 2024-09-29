import os
import uuid  # Import the uuid module for generating unique IDs
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.infrastructure.chroma.chroma_client import get_chroma_client
from openai import OpenAI

from src.infrastructure.settings import settings


def load_md_files_from_dir(directory_path):
    print("Loading documents")
    loader = DirectoryLoader(directory_path, glob="*.md")
    documents = loader.load()
    return documents


def segment_documents(documents, chunk_size=1000, chunk_overlap=200):
    print("Segmenting documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    segmented_docs = text_splitter.split_documents(documents)
    return segmented_docs


def batch_embeddings(items, batch_size: int = 2048):
    client = OpenAI(api_key=settings.openai_api_key)
    embeddings = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        res = client.embeddings.create(
            input=batch,
            model='text-embedding-3-small',
        )
        embeddings.extend([item.embedding for item in res.data])
    return embeddings


def upsert_to_chroma(segmented_docs, batch_size=100):
    chroma = get_chroma_client()  # Initialize Chroma client
    try:
        chroma.delete_collection("assistant")  # Delete the collection if it exists
    except Exception as e:
        print(f"Could not delete collection: {e}")

    collection = chroma.get_or_create_collection("assistant")  # Get or create the collection

    batch_documents = []  # List to hold document texts for batch upsert
    batch_ids = []  # List to hold unique IDs for the documents
    batch_embeddings_list = []  # List to hold embeddings for the documents

    # Generate embeddings for all segmented documents
    texts = [doc.page_content for doc in segmented_docs]  # Assuming 'page_content' contains the text
    embeddings = batch_embeddings(texts)

    for i, (doc, embedding) in enumerate(zip(segmented_docs, embeddings)):
        # Assign a unique ID using UUID
        unique_id = str(uuid.uuid4())  # Generate a new unique ID

        # Prepare to store the document text, ID, and embedding
        batch_documents.append(doc.page_content)  # Document text
        batch_ids.append(unique_id)  # Unique ID
        batch_embeddings_list.append(embedding)  # Corresponding embedding

        # Upsert when the batch size is reached
        if len(batch_documents) >= batch_size:
            collection.upsert(
                documents=batch_documents,
                ids=batch_ids,
                embeddings=batch_embeddings_list  # Assuming the method supports this parameter
            )
            print(f"Upserted {len(batch_documents)} documents")
            batch_documents.clear()  # Clear the batch after upsert
            batch_ids.clear()  # Clear the batch of IDs
            batch_embeddings_list.clear()  # Clear the batch of embeddings

    # Upsert any remaining documents in the last batch
    if batch_documents:
        collection.upsert(
            documents=batch_documents,
            ids=batch_ids,
            embeddings=batch_embeddings_list
        )
        print(f"Upserted {len(batch_documents)} documents")

    print("Upsert completed.")


if __name__ == "__main__":
    md_directory = "./src/infrastructure/llm/expert/train/data"
    documents = load_md_files_from_dir(md_directory)
    segmented_docs = segment_documents(documents)
    upsert_to_chroma(segmented_docs)
