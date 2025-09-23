from docx import Document
import os

def check_docx_files(folder_path):
    invalid_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            try:
                Document(file_path)
                print(f"[OK] {filename} is a valid .docx file.")
            except Exception as e:
                print(f"[ERROR] {filename} is NOT a valid .docx file: {e}")
                invalid_files.append(filename)
    if invalid_files:
        print("\nInvalid or corrupted .docx files detected:")
        for f in invalid_files:
            print(f" - {f}")
    else:
        print("\nAll .docx files are valid.")

if __name__ == "__main__":
    sample_docs_path = "sample_docs"  # adjust if your folder is elsewhere
    check_docx_files(sample_docs_path)
