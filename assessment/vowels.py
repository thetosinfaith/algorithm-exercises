list = ["a", "e", "i", "o", "u"]

user_input = input("Enter a letter: ")

if list != user_input:
    print(f"{user_input} is not a vowel")

    if user_input == list:
        print(f"{user_input} is a vowel")