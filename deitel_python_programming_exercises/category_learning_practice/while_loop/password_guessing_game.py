user_input = input("Enter a password: ")
correct_password = "secret123"

while user_input != correct_password:
    print("Incorrect password. Try again.")
    user_input = input("Enter a password: ")

print("Password accepted. Access granted!")
