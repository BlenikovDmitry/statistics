import PyPDF2
'''
пример чтения файла pdf
Совместим с последней версией Py2PDF(3.0.0)
'''
pdf = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf)
num_pages = len(pdf_reader.pages)

for page in range(num_pages):
    pdf_page = pdf_reader.pages[page]
    print(pdf_page.extract_text())


pdf.close()
