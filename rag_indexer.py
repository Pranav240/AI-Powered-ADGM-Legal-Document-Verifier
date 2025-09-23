import os
from pathlib import Path
from docx import Document
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Constants
DOCS_DIR = Path("sample_docs")
INDEX_FILE = "faiss.index"
MODEL_NAME = "all-MiniLM-L6-v2"  # Hugging Face sentence-transformers model
embedder = SentenceTransformer(MODEL_NAME)

def parse_docx(file_path):
    doc = Document(file_path)
    full_text = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
    return "\n".join(full_text)

def load_and_chunk_docs(docs_dir, chunk_size=500):
    texts = []
    metadatas = []
    for file_path in docs_dir.glob("*.docx"):
        text = parse_docx(file_path)
        if not text.strip():
            print(f"Skipping empty document: {file_path.name}")
            continue
        # Split text into fixed-size chunks
        for i in range(0, len(text), chunk_size):
            chunk = text[i : i + chunk_size]
            texts.append(chunk)
            metadatas.append({"source": file_path.name})
    return texts, metadatas

def embed_texts(texts):
    print("Embedding chunks with Hugging Face sentence-transformers...")
    embeddings = embedder.encode(texts)
    return np.array(embeddings).astype("float32")

def build_faiss_index():
    print("Loading documents...")
    texts, metadatas = load_and_chunk_docs(DOCS_DIR)
    print(f"Loaded {len(texts)} chunks from documents.")
    
    embeddings = embed_texts(texts)
    print("Building FAISS index...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    
    faiss.write_index(index, INDEX_FILE)
    print(f"FAISS index saved to {INDEX_FILE}.")

if __name__ == "__main__":
    build_faiss_index()
