import PyPDF2

'''
считываем данные из файла pdf
пишем в текстовый файл
'''

#чтение файла
pdf = open('example.pdf', 'rb')
#создаем объект reader
pdf_reader = PyPDF2.PdfReader(pdf)
#получаем число страниц
num_pages = len(pdf_reader.pages)

with open("out.txt", "w", encoding="utf-8") as file:
    file.write('')

with open('out.txt', 'w') as f:
    f.write('')

#в цикле выводим все страницы
for page in range(num_pages):
    pdf_page = pdf_reader.pages[page]
    pdf_extr = pdf_page.extract_text()
    with open("out.txt", "a", encoding="utf-8") as file:
        file.write(pdf_extr)
    

pdf.close()
