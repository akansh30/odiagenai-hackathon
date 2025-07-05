import PyPDF2
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file (either path or file-like).
    """
    text = ""

    if isinstance(uploaded_file, str):
        # It's a file path — keep it open until we're done
        with open(uploaded_file, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    else:
        # It's a file-like object (from Streamlit)
        reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()
