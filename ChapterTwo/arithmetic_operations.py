import sys

user_Input1 = int(input("Please, enter a number: "))
user_Input2 = int(input("Please, enter a number"))
user_Input3 = int(input("Please, enter a number"))

sums = user_Input1 + user_Input2 + user_Input3

average = sums / 3

product = user_Input1 * user_Input2 * user_Input3

smallest = -sys.maxsize
largest = sys.maxsize

if user_Input1 < user_Input2 and user_Input2 > user_Input3:
    smallest = user_Input1
elif user_Input2 < user_Input1 and user_Input1 > user_Input3:
    smallest = user_Input2
elif user_Input3 < user_Input1 and user_Input1 > user_Input2:
    smallest = user_Input3

print(sums)
print(average)
print(product)
print(smallest)
print(largest)

