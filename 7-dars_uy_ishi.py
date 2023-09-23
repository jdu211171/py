data = [
    {"full_name": "Eugene Elsmor", "company": "Kazu", "position": "Electrical Engineer", "salary": "$4440.86"},
    {"full_name": "Joni Stredder", "company": "JumpXS", "position": "Environmental Tech", "salary": "$870.05"},
    {"full_name": "Terri-jo Fulham", "company": "Tagchat", "position": "Assistant Media Planner", "salary": "$1992.55"},
    {"full_name": "Priscilla Pandya", "company": "Youopia", "position": "Help Desk Operator", "salary": "$3715.95"},
    {"full_name": "Wolfy Swanborough", "company": "Topic-lounge", "position": "Recruiter", "salary": "$1045.61"},
    {"full_name": "Raleigh Ratter", "company": "Zoozzy", "position": "Graphic Designer", "salary": "$602.41"},
    {"full_name": "Anastasia Winward", "company": "Avaveo", "position": "Cost Accountant", "salary": "$3641.42"},
    {"full_name": "Dorry Vasyunichev", "company": "Fivebridge", "position": "Junior Executive", "salary": "$2035.05"},
    {"full_name": "Richy Cleft", "company": "Jamia", "position": "Sales Associate", "salary": "$912.98"},
    {"full_name": "Zack Record", "company": "Oyonder", "position": "Social Worker", "salary": "$2492.23"},
    {"full_name": "Lissy Newns", "company": "Riffwire", "position": "Developer II", "salary": "$1177.79"},
    {"full_name": "Audrye Churchyard", "company": "Photospace", "position": "Environmental Tech", "salary": "$4125.83"},
    {"full_name": "Timothy Seligson", "company": "Riffpath", "position": "Compensation Analyst", "salary": "$1271.94"},
    {"full_name": "Brandie Rogeon", "company": "Riffpath", "position": "Analyst Programmer", "salary": "$1911.09"},
    {"full_name": "Dane Rugg", "company": "Twimm", "position": "Associate Professor", "salary": "$2200.72"},
    {"full_name": "Mick Jeduch", "company": "Realblab", "position": "Executive Secretary", "salary": "$1154.20"},
    {"full_name": "Rowland Christofol", "company": "Mycat", "position": "Senior Cost Accountant", "salary": "$1119.94"},
    {"full_name": "Sibella Abrahams", "company": "Minyx", "position": "Internal Auditor", "salary": "$4023.25"},
    {"full_name": "Layne Thomel", "company": "Centimia", "position": "Research Associate", "salary": "$4073.17"},
    {"full_name": "Demetris Clemenzi", "company": "Tagopia", "position": "Human Resources Manager",
     "salary": "$1530.37"},
    {"full_name": "Kerstin Devon", "company": "Katz", "position": "Senior Quality Engineer", "salary": "$1305.61"},
    {"full_name": "Brandon Burgwyn", "company": "Mydeo", "position": "Physical Therapy Assistant",
     "salary": "$1325.58"},
    {"full_name": "Dyana Crosby", "company": "Riffpath", "position": "Payment Adjustment Coordinator",
     "salary": "$1501.54"},
    {"full_name": "Harald Voller", "company": "Riffpedia", "position": "Accountant I", "salary": "$4397.60"},
    {"full_name": "Nollie Phipard-Shears", "company": "Aimbo", "position": "Legal Assistant", "salary": "$3172.57"},
    {"full_name": "Gaynor Dannohl", "company": "Riffpath", "position": "Administrative Assistant II",
     "salary": "$3035.89"},
    {"full_name": "Tome Bensen", "company": "Yamia", "position": "Assistant Professor", "salary": "$3677.10"},
    {"full_name": "Jessey Anshell", "company": "Bubblemix", "position": "Registered Nurse", "salary": "$2782.66"},
    {"full_name": "Valentijn Melbury", "company": "Bluejam", "position": "Statistician I", "salary": "$1308.43"},
    {"full_name": "Rochelle Andrejevic", "company": "Riffpath", "position": "VP Product Management",
     "salary": "$1734.61"}
]

# 1 - masala: Calculate how many people work in the Human Resources Manager department
# people_count = 0
# for dct in data:
#     if dct['position'] == 'Human Resources Manager':
#         people_count += 1
#
# print(people_count)

# 2 - masala: Calculate how much salary is paid to all employees working at Riffpath
# (note the $ sign in front of the salary)
# total_salary = 0
# for dct in data:
#     if dct['company'] == 'Riffpath':
#         total_salary += float(''.join(dct['salary'].replace('$', '')))
#
# print(total_salary)

# 3 - masala: Double the salary of employees whose name starts with "K"
# new_data = data.copy()
# for dct in new_data:
#     if dct['full_name'][0] == 'K':
#         new_salary_dict = {'salary': str(float(dct['salary'][1:]) * 2)}
#         dct.update(new_salary_dict)
#
# for dct in fio_data:
#     print(dct)

# 4 - masala: replace "full_name" keys with "FIO" but don't delete the values
# fio_data = [{"FIO": dct["full_name"], **{key: value for key, value in dct.items() if key != "full_name"}} for dct in data]
# for dct in fio_data:
#     print(dct)

# 5 - masala: delete all employees with the row "value" of key "position" -> "senior" or "junior"
# new_data = [{key: value for key, value in dct.items() if not any(substring in dct["position"] for substring in ['Senior', 'Junior'])} for dct in data]
# for count in range(new_data.count({})):
#     new_data.remove({})
# for dct in new_data:
#     print(dct)

# 6 - masala: Calculate the number of assistants
# number_of_assistants = 0
# for dct in data:
#     if any(substring in dct['position'] for substring in ['Assistant', 'assistant']):
#         number_of_assistants += 1
#
# print(number_of_assistants)


# 7 - masala: Move all "Assistant" to "Junior" position
# for example: "Assistant Professor" -> "Junior Professor"
# ranked_up_data = [{key: (value if not any(substring in dct['position'] for substring in ['Assistant']) else value.replace('Assistant', 'Junior')) for key, value in dct.items()} for dct in data]
#
# for dct in ranked_up_data:
#     print(dct)
