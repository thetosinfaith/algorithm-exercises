#Write a while loop that generates and prints random numbers between 1 and 10
# until it generates a number that is divisible by 7.
import random

user_input = random.randint

user_input = int(input("Enter a number: "))

while user_input < 0:

    print("Number is not divisible by 7!")

    user_input = int(input("Enter a number: "))

print(f"{user_input} is divisible by 7!")