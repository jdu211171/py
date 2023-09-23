# one = int(input('enter a number: '))
# two = int(input('enter a number: '))
# three = int(input('enter a number: '))
#
# if one >= two and one >= three:
#     print(one)
# elif two >= one and two >= three:
#     print(two)
# else:
#     print(three)

# == two ==
# palindrome_word = input('enter a word: ')
# print(palindrome_word == palindrome_word[::-1])

# == three ==
# some_text = input('enter a sentence: ')
# some_other_text = input('enter another sentence: ')
# if len(some_text) % 2 == 0 and len(some_other_text) % 2 == 1:
#     print(True)
# elif len(some_text) % 2 != 0 and len(some_other_text) % 2 != 1:
#     print(True)
# else:
#     print(False)

# == four ==
# number = int(input('enter a number: '))
# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Buzz')
# elif number % 5 == 0:
#     print('Fizz')
# else:
#     print('Error')

# == five ==
# some_text = 'salom bolalar salom'
# user_word = input('enter a word: ')
# if some_text.count(user_word) % 2 == 0:
#     print(some_text[::-1])
# else:
#     print(some_text.upper())

# == while one ==
# stop = int(input('enter a number: '))
# start = 1
# while start <= stop:
#     print(start * '*')
#     start += 1

# == while two ==
# integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# integers_count = 0
# letters_count = 0
# user_string = input('enter a string with numbers: ')
# index = len(user_string) - 1
# while index >= 0:
#     index -= 1
#     if user_string[index] == ' ':
#         continue
#     if integers.count(user_string[index]) > 0:
#         integers_count += 1
#     else:
#         letters_count += 1
# print('Raqam-> ', integers_count)
# print('Harf-> ', letters_count)

# == while three ==
# nt_num = int(input('enter a number for fibonacci: '))
# prev_num, current_num = 0, 1
# while nt_num > 0:
#     nt_num -= 1
#     prev_num, current_num = current_num, prev_num + current_num
#
# print(prev_num)

# == while four == prime number
# numb = int(input('enter a number: '))
# is_prime = True
# test_num = numb // 2 + 1
# while test_num > 2:
#     if numb % test_num == 0:
#         is_prime = False
#     test_num -= 1
# print(is_prime)

# == random ==
import random
# some_number = input('enter a number: ')
# reversed_some_number = some_number[::-1]
# print(f'{some_number} + {reversed_some_number} = {int(some_number) + int(reversed_some_number)}')

# sentence = input('enter a sentence: ')
# index = int(input('enter a index to remove:  '))
# print(sentence.replace(sentence[index], ''))

# lst = [5, 'salom', 90, True, 56.6]
# natija = 0
# for i in lst:
#     if isinstance(i, int) or isinstance(i, float):
#         natija += i
# print(natija)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = []
# for i in range(len(a)):
#     c.append(a[i] + b[i])
# enumerate()
# print(c)