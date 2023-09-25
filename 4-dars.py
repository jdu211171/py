
list1 = [1, 2, 3]
list2 = [11, 22, 33, 44, 55]
new_list = list()

# Loop through the indices of the shorter list
for i in range(min(len(list1), len(list2))):
  # Append a sublist with the elements from both lists at the same index
  new_list.append([list1[i], list2[i]])

print(new_list)