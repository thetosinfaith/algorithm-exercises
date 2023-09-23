email_address = input("Enter your email address: ")
correct_email_address = "user@example.com"

while email_address != correct_email_address:
    print("Invalid email address. Please enter a valid email address.")
    email_address = input("Enter your email address: ")

print("Thank you! Email address accepted.")