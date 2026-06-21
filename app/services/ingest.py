from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_OVERLAP, CHUNK_SIZE
from app.dependencies import get_vectorstore
from app.services.pdf import delete_temp_pdf


def ingest_pdf(file_path: Path, filename: str) -> dict:
    try:
        loader = PyPDFLoader(str(file_path))
        documents = loader.load()

        for doc in documents:
            doc.metadata["source"] = filename

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
        chunks = splitter.split_documents(documents)

        if not chunks:
            return {
                "message": "PDF processado, mas nenhum texto foi extraído.",
                "filename": filename,
                "chunks_indexed": 0,
            }

        get_vectorstore().add_documents(chunks)

        return {
            "message": "PDF indexado com sucesso.",
            "filename": filename,
            "chunks_indexed": len(chunks),
        }
    finally:
        delete_temp_pdf(file_path)
