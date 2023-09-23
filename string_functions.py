lst = [[0, 2, 0, 0], [0, 3, 2, 2], [2, 0, 10], [0, 1], [1], [2, 2, 2]]
count_lst = list()
for i in range(len(lst)):
    count_lst.append([lst[i].count(j) for j in lst[i]])

print(count_lst)
