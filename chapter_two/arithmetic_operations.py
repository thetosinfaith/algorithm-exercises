user_Input1 = int(input("Please, enter a number: "))
user_Input2 = int(input("Please, enter a number: "))
user_Input3 = int(input("Please, enter a number: "))

sums = user_Input1 + user_Input2 + user_Input3

average = sums / 3

product = user_Input1 * user_Input2 * user_Input3
smallest = min(user_Input1, user_Input2, user_Input3)
largest = max(user_Input1, user_Input2, user_Input3)

print(sums)
print(average)
print(product)
print(smallest)
print(largest)

