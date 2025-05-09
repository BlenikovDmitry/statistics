import csv

filename= 'result_ofz.csv'
filename_out = 'result.csv'
raw_data = []

def read_raw():
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)



def print_result(result):
    with open(filename_out, 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(result)


read_raw()
print_result(raw_data)
    

