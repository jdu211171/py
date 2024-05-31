floors = [[] for _ in range(11)]
for i in range(10):
    line = input("Enter the floors where the users go to: ")
    if line != "-":
        for floor in line.split(","):
            floors[int(floor)].append(floor)

for i in range(10, -1, -1):
    if floors[i]:
        print(",".join(floors[i]))
    else:
        print("-")
