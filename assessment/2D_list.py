new_list = [[0 for column(3) for row in range(2)]]

for row in range(2):
    for column in range(3):

        new_list[row][column] = row*column

        print(new_list)

