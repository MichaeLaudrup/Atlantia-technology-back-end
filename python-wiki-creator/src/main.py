from classes.DocxAlejandriaJSONPerspective import DocxAlejandriaJSONPerspective
from docx import Document
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
docx_path = os.path.join(current_dir, '../data/docs_wiki_inputs/maths_for_ia.docx')
doc = Document(docx_path)

alejandriaJSON = DocxAlejandriaJSONPerspective()

for paragraph in doc.paragraphs:
    paragraph_style = paragraph.style
    paragraph_text = paragraph.text
    alejandriaJSON.process_paragraph(paragraph_style, paragraph_text)