N = int(input("Enter the number of stations: "))
M = int(input("Enter the number of passengers: "))

routes = [0] * (N + 1)

for _ in range(M):
    name = input("Enter the passenger's name: ")
    entry = int(input("Enter the entry station number: "))
    exit = int(input("Enter the exit station number: "))

    for i in range(entry, exit):
        routes[i] += 1

max_passengers = max(routes)

print("Routes with the most passengers:")
for i in range(1, N + 1):
    if routes[i] == max_passengers:
        print(f"{i}-{i + 1}")
