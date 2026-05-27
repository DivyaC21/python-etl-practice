file = open("customers.txt", "r")

highest = 0

for row in file:

    data = row.strip().split(",")

    amount = int(data[2])

    if amount > highest:
        highest = amount

print("Highest Amount:", highest)

file.close()