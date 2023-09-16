language = input("Enter your language, please")
match language:
 case "yoruba":
    print("Welcome to Yoruba")

 case "Igbo":
     print("Welcome to English")

 case "Hausa":
     print("Welcome to French")

 case _:
     print("invalid input! Try again!")