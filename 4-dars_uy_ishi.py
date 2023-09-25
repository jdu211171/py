unordered_list = [[1, 3], [0, 0, 2], [7, 0], [2, 3]]
# print(max(max(unordered_list)))

str_list = ['alik', 'kim', 'it', 'web', 'arsenal', 'uzb']
# print(str_list[str_list.index(input('enter a value from string: '))])

first_list = [[], [1, 2, 3], [], [2, 0, 1, []]]
second_list = [[1, 2, 3], [2, 0, 1], [9, [1]]]


def recursive_sum(array):
    if isinstance(array, list):
        total = 0
        for value in array:
            total += recursive_sum(value)
        return total
    else:
        return array


# print(recursive_sum(1))

second_str_list = ['J', 'a', 'v', 'a']
print(''.join(second_str_list))
