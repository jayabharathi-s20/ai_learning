import os

from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
)


def load_document(file_path: str):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        loader = PyMuPDFLoader(file_path)

    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)

    elif extension == ".txt":
        loader = TextLoader(file_path)

    elif extension == ".csv":
        loader = CSVLoader(file_path)

    elif extension in [".xlsx", ".xls"]:
        loader = UnstructuredExcelLoader(file_path)

    elif extension in [".pptx", ".ppt"]:
        loader = UnstructuredPowerPointLoader(file_path)

    else:
        raise ValueError(f"Unsupported file format: {extension}")

    documents = loader.load()

    # Add custom metadata
    for document in documents:

        document.metadata["file_name"] = os.path.basename(file_path)
        document.metadata["file_format"] = extension.replace(".", "")

    return documents

def load_all_documents(folder_path):

    all_documents = []

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        print(f"Loading {file_name}...")

        try:
            documents = load_document(file_path)
            all_documents.extend(documents)

        except Exception as e:
            print(f"Skipping {file_name}: {e}")

    return all_documents