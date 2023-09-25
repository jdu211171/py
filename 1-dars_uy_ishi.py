import math

# Uy ishi:
# 1) Foydalanuvchi kiritgan radius asosida aylana maydonini hisoblaydigan Python dasturini yozing
print(math.pi * int(input('enter radius of a circle: ')) ** 2)
# 2) Foydalanuvchi kiritgan ma'lumotni uzunligicha kiritilgan ma'luotni ekranga chiqaring:
# Input: ab
# Output: abab
data = input('enter a data: ')
times = len(data)
print(data * times)
# 3) Input: Foundation
# Output: dnuoF noita
first_half = input('enter a string: ')
second_half = first_half[len(first_half)//2:]
first_half = first_half[0:len(first_half)//2:1]
print(first_half[::-1], second_half[::-1])
# 4) Foydalanuvchi tomonidan son qabul qilasiz
# Input: 4
# Output:
# 4x1 = 4
# 4 X 10 = 40
number = int(input('enter a number: '))
print(
    f"""
    {number} x 1 = {number * 1}
    {number} x 2 = {number * 2}
    {number} x 3 = {number * 3}
    {number} x 4 = {number * 4}
    {number} x 5 = {number * 5}
    {number} x 6 = {number * 6}
    {number} x 7 = {number * 7}
    {number} x 8 = {number * 8}
    {number} x 9 = {number * 9}
    {number} x 10 = {number * 10}
    """
)
# 5) Kiritilgan string ni birinchi va oxirgi elementini o'zaro o'zgartirib qayta o'zgaruvchiga o'zlashtiring
# Input:
# a = salomlar
# Output:
# a = ralomlas
my_string = input('a = ')
print('a = ' + my_string[-1] + my_string[1:-1] + my_string[0])