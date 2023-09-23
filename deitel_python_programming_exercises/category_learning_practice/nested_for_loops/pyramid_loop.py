pyramid_width = 15
for i in range(0, pyramid_width):
    for j in range(0, pyramid_width - i):
        print("  ", end=" ")
    for k in range(0, 2 * i + 1):
        print("0", end='')
    print(" ")

