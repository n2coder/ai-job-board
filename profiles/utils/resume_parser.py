import pdfplumber
import docx


def extract_text_from_pdf(file_path: str) -> str:
    text = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)

    return "\n".join(text)


def extract_text_from_docx(file_path: str) -> str:
    document = docx.Document(file_path)
    text = []

    for para in document.paragraphs:
        if para.text:
            text.append(para.text)

    return "\n".join(text)


def extract_resume_text(file_path: str) -> str:
    """
    Detect file type and extract resume text
    """
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported resume format")
