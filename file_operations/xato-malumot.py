import csv

# all false companies
with open('./xato-malumot.txt', newline='\r\n') as f:
    companies = f.read().split('\r\n')
    companies = csv.reader(companies)
    for company in companies:
        if int(company[2].split('-')[-1]) <= 2023:
            print(company)

# existing companies over 20 years
with open('./xato-malumot.txt', newline='\r\n') as f:
    companies = f.read().split('\r\n')
    companies = csv.reader(companies)
    for company in companies:
        if 2003 >= (int(company[2].split('-')[-1])) and 20 <= abs(int(company[2].split('-')[-1]) - 2023) and company[-1] == 'true':
            print(company)

# company names without repeat
with open('./xato-malumot.txt', newline='\r\n') as f:
    companies = f.read().split('\r\n')
    companies = csv.reader(companies)
    company_names = []
    for company in companies:
        company_names.append(company[0])
    company_names.sort()
    print(len(company_names))  # 100
    print(len(set(company_names)))  # 87
