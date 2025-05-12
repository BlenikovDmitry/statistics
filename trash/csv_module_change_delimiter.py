import csv
'''
скрипт тупо открывает файл с разделителями запятая
и меняет на разделитель точка с запятой
'''

def read():
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            raw.append(row)

def write():
    with open(filename_out, 'w', newline='') as f:
        spamwriter = csv.writer(f, delimiter=';')
        counter = 0
        while counter < len(raw):
            spamwriter.writerow(raw[counter])
            counter += 1

raw = []
filename = 'in.csv'
filename_out = 'out.csv'
read()
write()

print(1)

