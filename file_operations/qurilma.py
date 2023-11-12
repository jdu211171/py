import csv

with open('./qurilma.txt', newline='\r\n') as f:
    reader = csv.reader(f.read().split('\r\n'))
    for i in list(reader)[1:]:
        month = list(i)[-2].split('.')[1]
        if month in ['06', '07', '08']:
            print(i)