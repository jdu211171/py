int_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9

# print(sum(int_tuple))

# print(max(int_tuple) - min(int_tuple))

# no_max_tuple = list(int_tuple)
# no_max_tuple.remove(max(no_max_tuple))
# int_tuple = tuple(no_max_tuple)
# print(int_tuple)

# str_tuple = 'hello', 'Michael', 'how', 'Angelina', 'are', 'you', 'doing'
# over_five = list(i for i in str_tuple if len(i) > 5)
# print(over_five)

# sum_tuple = [(1, 3), (0, 2, 0), (1, 1, 1), (0, 4), (1, 9)]
# sum_tuple = [sum(i) for i in sum_tuple]
# print(sum_tuple)

# tuple_should_be_sorted = [(1, 2, 3), (2, 2), (3, 0, 0)]
# tuple_should_be_sorted = sorted(tuple_should_be_sorted, key=lambda value: sum(value))
# print(tuple_should_be_sorted)

# take_tuple = [(1, 2), (3, 4), (8, 9)]
# take_tuple = [list(value) for value in take_tuple]
# take_tuple[0].append(take_tuple[-1][0])
# take_tuple[1].append(take_tuple[-1][1])
# take_tuple.pop()
# take_tuple = [tuple(value) for value in take_tuple]
# print(take_tuple)

# sum_should_be_calculated = [[1, 2, 3], [4, 5, 6], [9, 27], [2, 0, 10], [0, 1], [1], [2, 2, 2], [99]]
# swap = sum(sum_should_be_calculated[0])
# result = tuple()
# for i in range(1, len(sum_should_be_calculated)):
#     if len(sum_should_be_calculated[i]) < 2:
#         continue
#     if swap < sum(sum_should_be_calculated[i]):
#         swap = sum(sum_should_be_calculated[i])
#         result = sum_should_be_calculated[i]
# print(result)

change_value = [(0, 2, 0, 0), (0, 3, 2, 2), (1, 3, 2, 4, 3), (4, 1, 2, 4)]
new_value = [list(value) for value in change_value]
for i in range(len(new_value)):
    for j in range(i):
        iteration = new_value[i].count(new_value[i][j])
        for k in range(iteration):
            new_value[i][new_value[i].index(j)] = iteration

print(new_value)
