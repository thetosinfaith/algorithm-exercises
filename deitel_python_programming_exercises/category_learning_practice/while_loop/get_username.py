name = input("Enter your name: ")

while name == " ":
    print("You did not enter your name")
    name = input(f"Enter your {name} : ")

print(f"Your name is {name}")
