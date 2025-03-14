from abc import ABC, abstractmethod

ALLOWED_EXTENSIONS = ['html', 'pdf', 'json', 'xml', 'txt']

class  AbstractRenderer(ABC):
    @abstractmethod
    def render(self):
        pass


class HTMLRenderer(AbstractRenderer):
    def render(self):
        print("Rendering HTML File")

class PdfRenderer(AbstractRenderer):
    def render(self):
        print("Rendering Pdf File")

class JsonRenderer(AbstractRenderer):
    def render(self):
        print("Rendering Json File")

class XmlRenderer(AbstractRenderer):
    def render(self):
        print("Rendering Xml File")

class TxtRenderer(AbstractRenderer):
    def render(self):
        print("Rendering Txt File")


class FileHandler:
    def __init__(self, file_name):
        self.filename = file_name

    @classmethod
    def create(cls, filename):
        if filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
            print("file not allowed")
        return cls(filename)
    
    def render(self):
        dict = {
            'html' : HTMLRenderer,
            'pdf' : PdfRenderer
        }
        handler = dict[self.filename.split('.')[-1]]
        return handler().render()
    


f1 = FileHandler.create('my.pdf')
f1.render()
f1 = FileHandler.create('my.html')
f1.render()
