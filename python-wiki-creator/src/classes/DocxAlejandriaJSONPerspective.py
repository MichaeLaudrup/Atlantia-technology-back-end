class DocxAlejandriaJSONPerspective:
    def __init__(self):
        self.subject_title = ""

    def process_paragraph(self, style, text):
        if style == "MainTitle":
            self.main_title = text
            
    def convert_to_json(self):
        return ""