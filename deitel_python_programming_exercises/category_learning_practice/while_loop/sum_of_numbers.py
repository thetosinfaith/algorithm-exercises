user_guess = int(input("Enter a number (or type 'stop' to finish): "))

result = 0
while user_guess != -1:
    user_guess = int(input("Enter a number (or type 'stop' to finish): "))
    result += user_guess

print(f"The sum of the numbers is {result} ")
