import aspose.words as aw
# pip install aspose-words
from pdf2docx import Converter
# pip install pdf2docx


def pdf2word():
    doc = aw.Document("Input.pdf")
    doc.save("Output.docx")

def pdfinword():
    pdf_file = 'input.pdf'
    docx_file = 'Output2.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


if __name__ == '__main__':
    pdfinword()

