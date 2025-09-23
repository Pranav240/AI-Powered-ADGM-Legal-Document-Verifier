How to Run the ADGM Corporate Document Checker Project
Step 1: Clone the Repository
Open your terminal and run:

bash
git clone https://github.com/Pranav240/AI-Powered-ADGM-Legal-Document-Verifier.git
cd AI-Powered-ADGM-Legal-Document-Verifier
Step 2: Create and Activate a Virtual Environment (Optional but Recommended)
Using Conda:

bash
conda create -n adgm_env python=3.9 -y
conda activate adgm_env
Or using venv:

bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
Step 3: Install Dependencies
Run the following command to install all required packages:

bash
pip install -r requirements.txt
Step 4: Prepare Documents
Add your .docx ADGM corporate documents to the sample_docs/ folder in the project root directory.

Step 5: Build the FAISS Vector Index
Generate the vector index of documents for semantic search by running:

bash
python rag_indexer.py
Look for messages indicating the embeddings and index are successfully created.

Step 6: Launch the Streamlit App
Start the web interface by running:

bash
streamlit run app.py
A browser window should open automatically displaying the document checker interface.

Step 7: Using the App
Upload your .docx corporate documents via the interface.

View checklist statuses for uploaded and missing documents.

Ask questions related to the uploaded documents using the AI-powered Q&A feature.

Additional Notes
No external API keys are required; all embeddings run locally using Hugging Face models.

After adding, modifying, or removing documents, rerun Step 5 (python rag_indexer.py) to refresh the index.

Always ensure your virtual environment is active before running commands.
