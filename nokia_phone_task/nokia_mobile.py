while True:
    print("Nokia 3310 App")
    print("""
        Display Menu
        1 -> PhoneBook
        2 -> Messages
        3 -> Chat
        4 -> Call Register
        5 -> Tones
        6 -> Settings
        7 -> Call Divert
        8 -> Games
        9 -> Calculator
        10 - > Reminders
        11 -> Clock
        12 -> Profiles
        13 -> Sim Services
        """)
    print("Press a number to get started")
    choice = input()

    if choice == "1":
        print("PhoneBook")
    elif choice == "2":
        print("Messages")
    elif choice == "3":
        print("Chat")
    elif choice == "4":
        print("Call Register")
    elif choice == "5":
        print("Tones")
    elif choice == "6":
        print("Settings")
    elif choice == "7":
        print("Call Divert")
    elif choice == "8":
        print("Games")
    elif choice == "9":
        print("Calculator")
    elif choice == "10":
        print("Reminders")
    elif choice == "11":
        print("Clock")
    elif choice == "12":
        print("Profiles")
    elif choice == "13":
        print("Sim Services")
    else:
        print("Wrong input! Try again")
