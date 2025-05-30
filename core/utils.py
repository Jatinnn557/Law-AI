from pypdf import PdfReader
import os, time
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()
os.environ['_BARD_API_KEY'] = os.getenv('_BARD_API_KEY')

def extract_text_from_pdf(pdf_path):
    text = []
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                cleaned = page_text.replace('\t\r', ' ').replace('\xa0', ' ')
                text.append(cleaned)
    return text

def chunk_text(text_list, max_chars=3000):
    chunks, current = [], ''
    for part in text_list:
        if len(current) + len(part) <= max_chars:
            current += ' ' + part
        else:
            chunks.append(current.strip())
            current = part
    if current:
        chunks.append(current.strip())
    return chunks

def process_pdf_and_summarize(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    summary = ''
    bard = Bard()
    for i, chunk in enumerate(chunks):
        prompt = f"Summarise in under 100 words:\n'''{chunk}'''"
        try:
            result = bard.get_answer(prompt)
            summary += f"--- Summary {i+1} ---\n{result['content']}\n\n"
            time.sleep(19)
        except Exception as e:
            summary += f"[Error in chunk {i+1}]: {e}\n"
    return summary

def classify_document(text):
    text = text.lower()
    if "divorce" in text:
        return "Divorce"
    elif "murder" in text or "homicide" in text:
        return "Murder"
    elif "land" in text or "property" in text:
        return "Land"
    else:
        return "Uncategorized"


def extract_text(uploaded_file):
    text = ""
    if uploaded_file.name.endswith('.pdf'):
        from PyPDF2 import PdfReader
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    elif uploaded_file.name.endswith('.docx'):
        import docx
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
    return text