# document_classifier.py
import json
import re

def load_document_types(json_path="utils/checklists.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["document_types"]

def classify_document(text, json_path="utils/checklists.json"):
    """
    Classify the document based on keyword matches.
    If multiple document types match, return the one with the highest score.
    """
    doc_types = load_document_types(json_path)
    text_lower = text.lower()

    best_match = None
    best_score = 0

    for doc_type, keywords in doc_types.items():
        score = 0
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw.lower()) + r"\b", text_lower):
                score += 1
        if score > best_score:
            best_score = score
            best_match = doc_type

    return best_match if best_match else "Unknown Document Type"
