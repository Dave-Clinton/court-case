from docx2pdf import convert
import os

def convert_docx_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)
