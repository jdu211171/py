print(
    f"""
    1 x 1 = {1 * 1}
    1 x 2 = {1 * 2}
    1 x 3 = {1 * 3}
    1 x 4 = {1 * 4}
    1 x 5 = {1 * 5}
    1 x 6 = {1 * 6}
    1 x 7 = {1 * 7}
    1 x 8 = {1 * 8}
    1 x 9 = {1 * 9}
    """
)

a = 3
b = 2
print(
    f"""
    {a} * {b} = {a * b}
    {a} / {b} = {a / b}
    {a} + {b} = {a + b}
    {a} - {b} = {a - b}
    {a} % {b} = {a % b}
    {a} // {b} = {a // b}
    {a} ** {b} = {a ** b}
    """
)

# print(a, b)
a, b = b, a
# print(a, b)

c = a + b
# print((a + b + c) // 3)

a = 74
b = 0
for i in range(2):
    b = b * 10 + a % 10
    a = a // 10

# print(b)

a = 4000
hour = a // (60 * 60)
a -= hour * 60 * 60
print(f'{hour} - hours')
minute = a // 60
a -= minute * 60
print(f'{minute} - minutes')
print(f'{a} - seconds')

a = 27
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
dates = [(i + a) % 32 if (i + a) % 32 != 0 else 1 for i in range(2,7)]
# print(dates)

# print(int(input('Enter a base: ')) ** int(input('Enter a power for a base: ')))

alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
# letter = input('kichkina harf kiriting: ')
# print('it\'s position in the alphabet is', alphabet[letter])