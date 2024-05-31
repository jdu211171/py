# dct = {
#     1: 10,
#     2: 20,
#     3: 30,
#     4: 55,
#     5: 25
# }
#
# dct_copy = dct.copy()
#
# for key in dct_copy:
#     if dct_copy[key] == max(dct_copy.values()):
#         dct.pop(key)
#     if dct_copy[key] == min(dct_copy.values()):
#         dct.pop(key)
#     print(key)
#
# print(dct)


# dict1 = {1: 10, 2: 20}
# dict2 = {3: 30, 4: 40}
# dict3 = {5: 50, 6: 60}
#
# dict4 = dict()
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)
#
# print(dict4)


# some_dct = {'data1': 100, 'data2': -54, 'data3': 247}
# result = sum(some_dct.values())
# print(result)


# dct = {
#     2: 10,
#     3: 20,
#     4: 30,
#     1: 55,
#     5: 25
# }
# # key_sorted_dct = {key: dct[key] for key in sorted(dct)}
# # key_sorted_dct = sorted(dct.items())
# value_sorted_dct = dict(sorted(list(dct.items()), key=lambda tpl: tpl[1]))
#
# print(value_sorted_dct)

# str1 = 'listen'
# cond = True
# str2 = 'silent'
#
# for i in str1:
#     if i not in str2:
#         print('Anagram emas')
#         cond = False
#         break
#
# if cond:
#     print('Anagram')

def recursive_array_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + recursive_array_sum(arr[1:])