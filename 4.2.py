# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = input('Введите действие: ')
#
# if c == "+":
#     x = a + b
#     print(x)
# elif c == "-":
#     x = a - b
#     print(x)
# elif c == "*":
#     x = a * b
#     print(x)
# elif c == "/":
#     x = a / b
#     print(x)
# else:
#     print('Я не понимаю')

# 2

curr_pos = input('Position: ')
target_pos = input('Target position: ')
row_diff = abs(int(target_pos[1]) - int(curr_pos[1]))
col_diff = abs(ord(target_pos[0]) - ord(curr_pos[0]))


if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
    print("Valid move for the knight.")
else:
    print("Invalid move for the knight.")
