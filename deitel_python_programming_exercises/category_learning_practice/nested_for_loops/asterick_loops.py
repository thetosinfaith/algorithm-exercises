y = 5
for row in range(y):
    print("", end="")
    for _ in range(row + 1):
        print("*", end="")
    print()

for row in range(y - 1, 0, -1):
    print("", end="")
    for _ in range(row):
        print("*", end="")
    print()
