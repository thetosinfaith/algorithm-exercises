#Exercises 3.1

user_input = 0
total_choices = 0
valid_choices = 0

while True:
    user_input = int(input("Enter a number (1 or 2), please: "))

    total_choices += 1

    if user_input == 1 or user_input == 2:
        valid_choices += 1
        break
    else:
        print("Invalid Input. Please, enter 1 or 2")

failures = total_choices - valid_choices
print(f"No of failures: {failures}")
