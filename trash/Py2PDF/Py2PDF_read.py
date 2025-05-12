import PyPDF2

'''
считываем данные из файла pdf
пишем в текстовый файл чтобы разбить построчно
считываем полученный файл и работать нужно будет уже с ним
'''
raw_data = []
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
    
f = open('out.txt',encoding="utf-8")
for line in f:
    raw_data.append(line)
print(raw_data)

counter = 0
while counter < 40:
    print(raw_data[counter])
    counter += 1
