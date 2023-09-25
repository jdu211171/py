'''contrary_prime_numbers = list()
prime_numbers = list()
def reverse_number(num):
    reversed_num_string = str(num)[::-1]
    reversed_num = int(reversed_num_string)
    return reversed_num


def reverse_prime_numbers(prime_numbers_list):
    list_of_reversed_prime_numbers = list()
    for num in prime_numbers_list:
        reversed_num = reverse_number(num)
        list_of_reversed_prime_numbers.append(reversed_num)
    return list_of_reversed_prime_numbers


for i in range(10, 100):
    count = 0
    for x in range(2, i - 1):
        if i % x == 0:
            count += 1
    if count == 0:
        prime_numbers.append(i)

reversed_prime_numbers = reverse_prime_numbers(prime_numbers)

for i in range(len(prime_numbers)):
    for j in range(len(reversed_prime_numbers)):
        if prime_numbers[i] == reversed_prime_numbers[j]:
            print(f'{prime_numbers[i]}: {reversed_prime_numbers[i]}')'''


def get_divisors_sum(n):
    divisors_sum = 1  # 1 is always a divisor, so initialize with 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid counting the same divisor twice
                divisors_sum += n // i
    return divisors_sum


friendly_numbers = []

for num in range(2, 50000):
    sum_of_divisors = get_divisors_sum(num)
    if sum_of_divisors < 50000 and get_divisors_sum(sum_of_divisors) == num and num != sum_of_divisors:
        friendly_numbers.append((num, sum_of_divisors))


# print("Friendly numbers less than 50,000:")
# for pair in friendly_numbers:
#     print(pair)

def are_friendly_numbers(num1, num2):
    sum1 = get_divisors_sum(num1)
    sum2 = get_divisors_sum(num2)
    return sum1 == num2 and sum2 == num1


# Example usage:
num1 = 5564
num2 = 5020

# if are_friendly_numbers(num1, num2):
#     print(f"{num1} and {num2} are friendly numbers.")
# else:
#     print(f"{num1} and {num2} are not friendly numbers.")

some_list = [True, "Salom", 5, 5.6]
new_list = list()
for i in some_list:
    new_list.append(type(i))

# print(new_list)

some_numbers = [7, 8, 1, 3, 4, 6, 7, 5]
new_numbers = list()
for i in range(len(some_numbers)):
    new_numbers.append(some_numbers[i] ** 2) if i % 2 == 0 else new_numbers.append(some_numbers[i] ** 3)

# print(some_numbers)
# print(new_numbers)

unordered_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
ordered_list = list()
unordered_list.sort()
unordered_list.reverse()
# print(unordered_list)
# for i in unordered_list:

biggest_value = [2, 1, -4, -9, 0, -5, 8, 3]
biggest_value.sort()
# print(biggest_value[-2])

repeated_list = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]

for i in repeated_list:
    for j in range(1, len(repeated_list) - 1):
        if j == repeated_list.index(i):
            continue
        if i == repeated_list[j]:
            repeated_list.remove(repeated_list[j])

# print(repeated_list)


fix_repeated_list = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
unique_list = list(set(repeated_list))
# print(unique_list)

a = [1, 2]
b = a.copy()
b.remove(2)
# print(a, b)

sample_list = [11, 33, 50]
expected_list = str()
for i in range(len(sample_list)):
    expected_list += str(sample_list[i])

# print(expected_list)

first_list = [1, 1, 3, 4, 4, 5, 6, 7]
second_list = [0, 1, 2, 3, 4, 4, 5, 7, 8]

middle_arithmetic = first_list + second_list

divider = len(middle_arithmetic)
sum = 0
for i in middle_arithmetic:
    sum += i

middle_arithmetic = sum
print(middle_arithmetic // divider)