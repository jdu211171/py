import csv

# employees who hired at age 18 and above
with open('ishga_kirgan.txt', newline='\r\n') as f:
    employees = f.read().split('\r\n')
    employees = csv.reader(employees)
    result = []
    for employee in list(employees):
        if abs(int(employee[-1].split('-')[-1]) - int(employee[-2].split('-')[-1])) >= 18:
            print(employee)

# woman employees who have worked more than 20 years
with open('ishga_kirgan.txt', newline='\r\n') as f:
    employees = f.read().split('\r\n')
    employees = csv.reader(employees)
    result = []
    for employee in list(employees):
        if abs(int(employee[-1].split('-')[-1]) - 2023) >= 20 and employee[1] == 'Female':
            print(employee)
