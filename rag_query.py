import os
from pathlib import Path
from google import genai
import faiss
import numpy as np

INDEX_DIR = Path("faiss_index")
EMBED_MODEL = "gemini-embedding-001"
GEN_MODEL = "gemini-1.5"  # Or your available Gemini generation model

client = genai.Client()

def load_faiss_index():
    index = faiss.read_index(str(INDEX_DIR / "index.faiss"))
    with open(INDEX_DIR / "metadata.txt", "r", encoding="utf-8") as f:
        metadatas = [line.strip() for line in f]
    return index, metadatas

def embed_query(text):
    response = client.embeddings.embed_texts(
        model=EMBED_MODEL,
        texts=[text]
    )
    return np.array(response.data[0].embedding, dtype=np.float32).reshape(1, -1)

def retrieve_top_k(index, metadatas, query_embedding, k=4):
    distances, indices = index.search(query_embedding, k)
    results = []
    for idx in indices[0]:
        if idx < len(metadatas):
            results.append(metadatas[idx])
    return results

def generate_answer(question, context_docs):
    context_text = "\n\n---\n\n".join(context_docs)
    prompt = f"""You are an assistant using the following documents as context. Answer ONLY based on these. If the answer is not in the context, say so.

Context:
{context_text}

Question:
{question}

Answer concisely and cite sources if possible.
"""
    response = client.models.generate_content(
        model=GEN_MODEL,
        contents=prompt
    )
    return response.text

def answer_question(question):
    index, metadatas = load_faiss_index()
    query_emb = embed_query(question)

    # For simplicity, load full docs from file paths (you may want smarter caching)
    top_sources = retrieve_top_k(index, metadatas, query_emb, k=4)
    context_chunks = []
    for src in top_sources:
        try:
            with open(src, "r", encoding="utf-8") as f:
                context_chunks.append(f.read())
        except Exception as e:
            context_chunks.append(f"[Could not load document {src}]")

    answer = generate_answer(question, context_chunks)
    return answer, top_sources

if __name__ == "__main__":
    q = "What documents are required for company incorporation?"
    ans, docs = answer_question(q)
    print("ANSWER:\n", ans)
    print("\nRETRIEVED SOURCES:")
    for d in docs:
        print("-", d)
