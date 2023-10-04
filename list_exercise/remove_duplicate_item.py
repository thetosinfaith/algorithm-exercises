items_on_list = [15, 20, 25, 20, 10, 5]

new_list = []

for duplicates in items_on_list:
    if duplicates not in new_list:
        new_list.append(duplicates)

        print(new_list)

# correct the logical error in the code
