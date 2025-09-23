How to Run the ADGM Corporate Document Checker Project
Clone the repository

Open terminal and run:

text
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create and activate a virtual environment (Recommended)

Using conda:

text
conda create -n adgm_env python=3.9 -y
conda activate adgm_env
Or using venv:

text
python -m venv venv
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows
Install dependencies

text
pip install -r requirements.txt
Prepare the documents

Place your .docx ADGM corporate documents inside the folder named sample_docs/ in the project root.

Build the FAISS vector index

Run the indexer to embed documents for semantic search:

text
python rag_indexer.py
Watch for logs confirming successful embedding and index creation.

Start the Streamlit app

Launch the web UI for uploading and checking documents:

text
streamlit run app.py
This will open a browser window with the document checker interface.

Use the app

Upload .docx corporate documents.

View checklist status for uploaded and missing documents.

Ask questions about your documents using the AI-powered Q&A.

Additional notes

No API keys needed; embeddings run locally with Hugging Face.

After adding or removing documents, rerun step 5 to update the search index.

Ensure your virtual environment is activated when running scripts.