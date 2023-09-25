# 1-masala: Listning ichidagi tuple ma'lumotlarni listga o'girib beradigan dastur tuzing.
# Input: [(1,2),(2,3), (3,4)]
# Output: [[1,2],[2,3],[3,4]]
tpl = [(1, 2), (2, 3), (3, 4)]
lst = [list(value) for value in tpl]
# print(lst)

# 2-masala:
chars = ['p', 'q']
num = 4
combined_list = list()
for i in range(num):
    combined_list.append(f'{chars[0]}{i + 1}')
    combined_list.append(f'{chars[1]}{i + 1}')
# print(combined_list)

# 3-masala:
dala = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8]
etak = list()
tarozi = list()
for i in range(len(dala) - 1):
    etak.append(dala[i])
    if dala[i] >= dala[i + 1]:
        tarozi.append(etak)
        etak = list()
etak.append(dala[-1])
tarozi.append(etak)
# print([value for value in tarozi if len(value) > 1])

# change_value = [(0, 2, 0, 0), (0, 3, 2, 2), (1, 3, 2, 4, 3), (4, 1, 2, 4)]
# new_value = [list(value) for value in change_value]
# for i in new_value:
#     for j in i:
#         iteration = i.count(j)
#         for k in range(iteration):
#             i[i.index(j)] = iteration
change_value = [(0, 2, 0, 0), (0, 3, 2, 2), (1, 3, 2, 4, 3), (4, 1, 2, 4)]
new_value = [list(value) for value in change_value]
for i in range(len(new_value)):
    counts = [new_value[i].count(j) for j in new_value[i]]
    new_value[i] = counts

print(new_value)
