import streamlit as st
import os
import json
from docx import Document

# Load the checklists.json file
with open("utils/checklists.json", "r") as f:
    checklists_data = json.load(f)

document_types = checklists_data.get("document_types", {})
process_checklists = checklists_data.get("process_checklists", {})

def classify_document(doc_text):
    """Classify document based on keywords in document_types."""
    for doc_type, keywords in document_types.items():
        for keyword in keywords:
            if keyword.lower() in doc_text.lower():
                return doc_type
    return "Unknown"

def read_docx(file_path):
    """Read all text from a .docx file."""
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

st.title("📄 ADGM Corporate Document Checker")

uploaded_files = st.file_uploader("Upload your documents", type=["docx"], accept_multiple_files=True)

if uploaded_files:
    uploaded_doc_types = set()

    for uploaded_file in uploaded_files:
        file_path = os.path.join("sample_docs", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        doc_text = read_docx(file_path)
        doc_type = classify_document(doc_text)
        uploaded_doc_types.add(doc_type)

        st.write(f"**File:** {uploaded_file.name} → **Classified as:** {doc_type}")

    st.markdown("---")
    st.subheader("Checklist Status")

    for process, required_docs in process_checklists.items():
        st.markdown(f"### 📂 {process}")

        uploaded_in_process = [d for d in required_docs if d in uploaded_doc_types]
        missing_in_process = [d for d in required_docs if d not in uploaded_doc_types]

        # Green for uploaded
        if uploaded_in_process:
            st.markdown(f"✅ **Uploaded:** <span style='color:green'>{', '.join(uploaded_in_process)}</span>", unsafe_allow_html=True)
        else:
            st.markdown("✅ **Uploaded:** None")

        # Red + Bold for missing
        if missing_in_process:
            st.markdown(f"❌ **Missing:** <span style='color:red; font-weight:bold'>{', '.join(missing_in_process)}</span>", unsafe_allow_html=True)
        else:
            st.markdown("❌ **Missing:** None")

        st.markdown("---")
