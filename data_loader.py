import json
import re
from pathlib import Path
from pypdf import PdfReader

PDF_PATH = "Data Sources.pdf"
JSON_PATH = "utils/checklists.json"

def extract_data_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_document_entries(text):
    """
    Extracts (Category, Document Name, URL) from PDF text.
    - Handles URLs split across lines
    - Works even if no URL is present
    """
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    current_category = None
    entries = []
    pending_doc = None

    url_pattern = re.compile(r"https?://\S+")

    for line in lines:
        # Detect category lines
        if line.isupper() or "Company" in line or "Employment" in line or "Policy" in line:
            current_category = line
            continue

        # If line has a URL and pending doc
        if pending_doc and url_pattern.search(line):
            url = url_pattern.search(line).group()
            entries.append((current_category or "Uncategorized", pending_doc, url))
            pending_doc = None
            continue

        # If line has both doc name and URL
        match = re.match(r"(.+?)\s+(https?://\S+)", line)
        if match:
            name = match.group(1).strip()
            url = match.group(2).strip()
            entries.append((current_category or "Uncategorized", name, url))
            pending_doc = None
            continue

        # If line only has a document name (store temporarily)
        if not url_pattern.search(line):
            pending_doc = line

    # Add any leftover doc without URL
    if pending_doc:
        entries.append((current_category or "Uncategorized", pending_doc, ""))

    return entries


def update_checklists_json(entries, json_path):
    if not Path(json_path).exists():
        data = {"document_types": {}, "process_checklists": {}}
    else:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    process_checklists = {}

    for category, name, url in entries:
        # Add document type keywords
        keywords = [name.lower()]
        data["document_types"][name] = keywords

        # Group by category for process_checklists
        if category not in process_checklists:
            process_checklists[category] = []
        process_checklists[category].append(name)

    # Merge with existing
    data["process_checklists"].update(process_checklists)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Updated {json_path} with {len(entries)} entries and {len(process_checklists)} processes.")

if __name__ == "__main__":
    text = extract_data_from_pdf(PDF_PATH)
    entries = parse_document_entries(text)
    update_checklists_json(entries, JSON_PATH)
