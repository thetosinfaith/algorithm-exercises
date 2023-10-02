def main_menu():
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
    Input = int(input())

    if Input == 1:
        print("""
            1 -> Search
            2 -> Service Nos
            3 -> Add Name
            4 -> Erase
            5 -> Edit
            6 -> Assign Tone
            7 -> Send B' Card
            8 -> Options
            9 -> Speed Dials
            10 -> Voice Tags
            """)
        print("pick number 1: ")
        Input = int(input())

        if Input == 1:
            print("Search")
        elif Input == 8:
            print("""
                1 -> Type of view
                2 -> Memory status
                """)
    elif Input == 2:
        print("""
            1 -> Write Messages
            2 -> Inbox
            3 -> Outbox
            4 -> Picture messages
            5 -> Templates
            6 -> Smileys
            7 -> Message Settings
            """)
        print("Pick number 7")
        Input = int(input())

        if Input == 7:
            print("""
                1 -> Set
                2 -> Common
                """)
            print("Pick an option")
            Input = int(input())

            if Input == 1:
                print("""
                    1 -> Message centre number
                    2 -> Message sent as
                    3 -> Message validity
                    """)
            elif Input == 2:
                print("""
                    1 -> Delivery reports
                    2 -> Reply via same centre
                    3 -> Character support
                    """)
    elif Input == 3:
        print("""
            1 -> Chat
            """)
        print("Pick an option")
        Input = int(input())
    elif Input == 4:
        print("""
            1 -> Missed Calls
            2 -> Received Calls
            3 -> Dialled Numbers
            4 -> Erase recent call lists
            5 -> Show call duration
            6 -> Show call cost
            7 -> Call cost setting
            8 -> Prepaid credit
            """)
        print("Use number 5 to check call duration")
        Input = int(input())

        if Input == 5:
            print("""
                1 -> Last call duration 
                2 -> All calls duration
                3 -> Received calls duration
                4 -> Dialled calls duration
                5 -> Clear timers
                """)
            print("Pick an option")
            Input = int(input())
        elif Input == 6:
            print("""
                1 -> Last call cost
                2 -> All calls cost
                3 -> Clear counters
                """)
            print("Pick an option")
            Input = int(input())
        elif Input == 7:
            print("""
                1 -> Call cost limit
                2 -> Show costs in
                """)
            Input = int(input())
    elif Input == 5:
        print("""
            1 -> Ringing Tone
            2 -> Ringing Volume
            3 -> Incoming Call alert
            4 -> Composer
            5 -> Message alert tone
            6 -> Keypad tones
            7 -> Warning and game tones
            8 -> Vibrating alert
            9 -> Screen saver
            """)
        print("Press an option")
        Input = int(input())
    elif Input == 6:
        print("""
            1 -> Call setting
            2 -> Phone setting
            3 -> Security setting
            4 -> Restore factory setting
            """)
        print("Pick an option to continue")
        Input = int(input())

        if Input == 1:
            print("""
                1 -> Automatic redial
                2 -> Speed dialling
                3 -> Call waiting options
                4 -> Phone line in use
                5 -> Automatic answer
                """)
            print("Pick an option to continue")
            Input = int(input())

            if Input == 2:
                print("""
                    1 -> Language
                    2 -> Cell info display
                    3 -> Welcome note 
                    4 -> Network selection
                    5 -> Lights
                    6 -> Confirm SIM service actions
                    """)
                print("Pick an option to continue")
                Input = int(input())
            elif Input == 3:
                print("""
                    1 -> PIN Code request
                    2 -> Call barring service
                    3 -> Fixed dialling
                    4 -> Closed user group
                    5 -> Phone security
                    6 -> Change access codes
                    """)
                print("Pick an option to continue")
                Input = int(input())
    elif Input == 11:
        print("""
            1 -> Alarm Clock
            2 -> Clock Setting
            3 -> Date setting
            4 -> Stopwatch
            5 -> Countdown timer
            6 -> Auto update of date and time
            """)
        print("Enter a number to get started")
        Input = int(input())
    else:
        print("Wrong input! Try again")


if __name__ == "__main__":
    main_menu()

