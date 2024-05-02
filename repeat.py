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

input_num = input()
dimensions = [int(x) for x in input_num.split(',')]
row_num = dimensions[0]  # 3
col_num = dimensions[1]  # 5
multilist = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multilist[row][col] = row * col
