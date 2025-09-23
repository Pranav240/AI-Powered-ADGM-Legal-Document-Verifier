# checklist_checker.py
import json

def load_checklists(json_path="utils/checklists.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["process_checklists"]

def check_missing_documents(process_name, uploaded_doc_types, json_path="utils/checklists.json"):
    checklists = load_checklists(json_path)
    required_docs = checklists.get(process_name, [])
    missing_docs = [doc for doc in required_docs if doc not in uploaded_doc_types]
    return required_docs, missing_docs
