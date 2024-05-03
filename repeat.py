# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=', ')

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(8))

# def create_dict(n):
#     dct = {}
#     for i in range(1, n + 1):
#         dct[i] = i * i
#     return dct
#
#
# print(create_dict(8))

# def tuple_creator(values):
#     values = values.split(',')
#     values = tuple(values)
#     return values
#
#
# print(tuple_creator('34,67,55,33,12,98'))

# class InputOutString:
#     def __init__(self):
#         self.s = ''
#
#     def get_string(self):
#         self.s = input()
#
#     def print_string(self):
#         print(self.s.upper())

# import math
# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
# print(','.join(value))

# input_num = input()
# dimensions = [int(x) for x in input_num.split(',')]
# row_num = dimensions[0]  # 3
# col_num = dimensions[1]  # 5
# multilist = [[0 for col in range(col_num)] for row in range(row_num)]
# for row in range(row_num):
#     for col in range(col_num):
#         multilist[row][col] = row * col
#
# print(multilist)

# question 8
# def print_sorted_words():
#     words = input().split(',')
#     words.sort()
#     print(','.join(words))
#
#
# print_sorted_words()

# question 9
# def print_capitalized_word():
#     words = input().split(' ')
#     words = [word.upper() for word in words]
#     print(' '.join(words))
#
#
# print_capitalized_word()

# question 10
# def print_sorted_white_space_separated_words():
#     words = input().split(' ')
#     words.sort()
#     words = set(words)
#     print(' '.join(words))
#
#
# print_sorted_white_space_separated_words()

# question 11
# binary_numbers = input("Enter comma separated 4 digit binary numbers: ").split(',')
# divisible_by_five = []
# for binary_number in binary_numbers:
#     decimal_number = int(binary_number, 2)
#     if decimal_number % 5 == 0:
#         divisible_by_five.append(binary_number)
#
# print(','.join(divisible_by_five))

# question 12
# even_numbers = []
#
# for number in range(1000, 3001):
#     str_number = str(number)
#     is_even = True
#     for digit in str_number:
#         if int(digit) % 2 != 0:
#             is_even = False
#             break
#     if is_even:
#         even_numbers.append(str_number)
#
# print(','.join(even_numbers))

# question 13
# def calculate_letters_and_digits_from_string():
#     string = input("Enter a string: ")
#     letters = 0
#     digits = 0
#     for character in string:
#         if character.isalpha():
#             letters += 1
#         elif character.isdigit():
#             digits += 1
#
#     print(f"LETTERS: {letters}\nDIGITS: {digits}")
#
#
# calculate_letters_and_digits_from_string()

# question 14
# def calculate_uppercase_and_lowercase():
#     string = input("Enter a string: ")
#     uppercase = 0
#     lowercase = 0
#     for character in string:
#         if character.isupper():
#             uppercase += 1
#         elif character.islower():
#             lowercase += 1
#
#     print(f"UPPERCASE: {uppercase}\nLOWERCASE: {lowercase}")
#
#
# calculate_uppercase_and_lowercase()


# question 15
# a = int(input("Enter a single digit: "))
#
# n = 4
# r = 0
# # result = a * (1 - r**n) / (1 - r)
# # a_n = a + (n - 1) * d
# # S_n = n/2 * (2a + (n - 1) * d)
# result = a * (1 + 11 + 111 + 1111)
# print("The result is:", result)

# question 16
# numbers = input("Enter comma separated numbers: ").split(',')
#
# squared_odds = [int(num)**2 for num in numbers if int(num) % 2 != 0]
#
# print(','.join(map(str, squared_odds)))

# question 17
# net_amount = 0
#
# while True:
#     transaction = input("Enter a transaction (D for deposit, W for withdrawal) or 'quit' to finish: ")
#
#     if transaction.lower() == 'quit':
#         break
#
#     transaction_type, amount = transaction.split()
#
#     if transaction_type.lower() == 'd':
#         net_amount += int(amount)
#     elif transaction_type.lower() == 'w':
#         net_amount -= int(amount)
#
# print("The net amount is:", net_amount)

# question 18
# import re
#
#
# def validate_passwords(passwords):
#     valid_passwords = []
#     for password in passwords:
#         if len(password) < 6 or len(password) > 12:
#             continue
#         elif not re.search("[a-z]", password):
#             continue
#         elif not re.search("[0-9]", password):
#             continue
#         elif not re.search("[A-Z]", password):
#             continue
#         elif not re.search("[$#@]", password):
#             continue
#         else:
#             valid_passwords.append(password)
#     return valid_passwords
#
#
# passwords = input("Enter comma separated passwords: ").split(',')
#
# valid_passwords = validate_passwords(passwords)
#
# print(','.join(valid_passwords))

# question 19
# from operator import itemgetter
#
# data = []
# while True:
#     line = input()
#     if line == "":
#         break
#     name, age, height = line.split(',')
#     data.append((name, int(age), int(height)))
#
# data.sort(key=itemgetter(0, 1, 2))  # sort by name, then by age, then by height
#
# print(data)

# question 20
# class DivisibleBySeven:
#     def __init__(self, n):
#         self.n = n
#
#     def divisible_by_seven(self):
#         for i in range(0, self.n):
#             if i % 7 == 0:
#                 yield i
#
#
# divisible = DivisibleBySeven(100)
# for number in divisible.divisible_by_seven():
#     print(number)

def divisible_by_seven(number):
    for i in range(0, number):
        if i % 7 == 0:
            yield i


print(list(divisible_by_seven(100)))