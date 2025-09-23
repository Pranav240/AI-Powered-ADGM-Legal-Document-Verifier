**ADGM Corporate Document Checker**



**Project Overview**

This project is an AI-powered document checking assistant designed to help businesses comply with Abu Dhabi Global Market (ADGM) regulations for corporate document submission. 



It allows users to upload important corporate documents in `.docx` format, automatically classifies them, verifies the presence of required documents per ADGM checklists, and reports missing documents clearly. 



The system uses local Hugging Face embeddings and FAISS for fast document retrieval and search, with no reliance on cloud API keys or external paid services.



**Features**

\- Upload multiple `.docx` business documents.

\- Automatic document type classification based on keyword matching.

\- Checklist validation against ADGM categories like Incorporation, Employment, Data Protection, and more.

\- Highlights missing required documents per category.

\- Retrieval Augmented Generation (RAG) based question answering on uploaded documents.

\- Runs entirely on local machine with open-source libraries.

