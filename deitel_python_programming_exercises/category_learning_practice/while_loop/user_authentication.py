user_name = input("Username: ")
password = input("Password: ")

correct_username = "user456"
correct_password = "correctpass"

while user_name != correct_username and password != correct_password:
    print("Incorrect credentials. Try again.")
    user_name = input("Username: ")
    password = input("Password: ")

print("Authentication successful. Welcome, user456!")