from langchain_community.document_loaders import (
    PyMuPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter


def print_chunks(chunks):
    print(f"\nTotal Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks, start=1):
        print(f"========== Chunk {i} ==========")
        print(chunk.page_content)
        print("=" * 80)


def get_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)



def load_pdf():
    pdf_path = r"/home/bitcot/Documents/AI_LEARNING_FOLDER/ai_learning/week_01/day_05/data/ai_learning.pdf"  

    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    chunks = get_chunks(documents)
    print_chunks(chunks)

    return chunks



def load_docx():
    docx_path = r"/home/bitcot/Documents/AI_LEARNING_FOLDER/ai_learning/week_01/day_05/data/ai_learning.docx"

    loader = Docx2txtLoader(docx_path)
    documents = loader.load()

    chunks = get_chunks(documents)
    print_chunks(chunks)

    return chunks



def load_txt():
    txt_path = r"/home/bitcot/Documents/AI_LEARNING_FOLDER/ai_learning/week_01/day_05/data/ai_learning.txt"

    loader = TextLoader(txt_path)
    documents = loader.load()

    chunks = get_chunks(documents)
    print_chunks(chunks)

    return chunks


def load_csv():
    csv_path = r"/home/bitcot/Documents/AI_LEARNING_FOLDER/ai_learning/week_01/day_05/data/ai_learning.csv"

    loader = CSVLoader(csv_path)
    documents = loader.load()

    chunks = get_chunks(documents)
    print_chunks(chunks)

    return chunks



def load_xlsx():
    xlsx_path = r"/home/bitcot/Documents/AI_LEARNING_FOLDER/ai_learning/week_01/day_05/data/1mb.xlsx" 

    loader = UnstructuredExcelLoader(xlsx_path)
    documents = loader.load()

    chunks = get_chunks(documents)
    print_chunks(chunks)

    return chunks

def load_pptx():
    pptx_path = r"/home/bitcot/Documents/AI_LEARNING_FOLDER/ai_learning/week_01/day_05/data/ai_learning.pptx"

    loader = UnstructuredPowerPointLoader(pptx_path)
    documents = loader.load()

    chunks = get_chunks(documents)
    print_chunks(chunks)

    return chunks


if __name__ == "__main__":
    # load_pdf()
    # load_docx()
    # load_txt()
    # load_csv()
    # load_xlsx()
    load_pptx()