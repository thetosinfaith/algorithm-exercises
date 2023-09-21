ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
for i in range(0, len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[i] > ls[j]:
            print(ls)
