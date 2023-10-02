def display_menu():
    print("Nokia 3310 App")
    print("Display Menu")
    print("1 -> PhoneBook")
    print("2 -> Messages")
    print("3 -> Chat")
    print("4 -> Call Register")
    print("5 -> Tones")
    print("6 -> Settings")
    print("7 -> Call Divert")
    print("8 -> Games")
    print("9 -> Calculator")
    print("10 -> Reminders")
    print("11 -> Clock")
    print("12 -> Profiles")
    print("13 -> Sim Services")
    print("Press a number to get started")
    return input()


def phonebook_menu():
    print("PhoneBook Menu")
    print("1 -> Search")
    print("2 -> Service Nos")
    print("3 -> Add Name")
    print("4 -> Erase")
    print("5 -> Edit")
    print("6 -> Assign Tone")
    print("7 -> Send B' Card")
    print("8 -> Options")
    print("9 -> Speed Dials")
    print("10 -> Voice Tags")
    print("B -> Back")
    print("pick a number: ")
    return input()

def phonebook_options_menu():
    print("PhoneBook Options Menu")
    print("1 -> Type of view")
    print("2 -> Memory status")
    print("B -> Back")
    print("pick a number: ")
    return input()

def messages_menu():
    print("Messages Menu")
    print("1 -> Write Messages")
    print("2 -> Inbox")
    print("3 -> Outbox")
    print("4 -> Picture messages")
    print("5 -> Templates")
    print("6 -> Smileys")
    print("7 -> Message Settings")
    print("B -> Back")
    print("Pick number 7")
    return input()


def message_settings_menu():
    print("Message Settings Menu")
    print("1 -> Set")
    print("2 -> Common")
    print("B -> Back")
    print("Pick an option")
    return input()


def message_settings_common_menu():
    print("Common Menu")
    print("1 -> Message centre number")
    print("2 -> Message sent as")
    print("3 -> Message validity")
    print("B -> Back")
    print("Pick an option")
    return input()


def call_register_menu():
    print("Call Register Menu")
    print("1 -> Missed Calls")
    print("2 -> Received Calls")
    print("3 -> Dialled Numbers")
    print("4 -> Erase recent call lists")
    print("5 -> Show call duration")
    print("6 -> Show call cost")
    print("7 -> Call cost setting")
    print("8 -> Prepaid credit")
    print("B -> Back")
    print("Use number 5 to check call duration")
    return input()


def call_duration_menu():
    print("Call Duration Menu")
    print("1 -> Last call duration")
    print("2 -> All calls duration")
    print("3 -> Received calls duration")
    print("4 -> Dialled calls duration")
    print("5 -> Clear timers")
    print("B -> Back")
    print("Pick an option")
    return input()


def call_cost_menu():
    print("Call Cost Menu")
    print("1 -> Last call cost")
    print("2 -> All calls cost")
    print("3 -> Clear counters")
    print("B -> Back")
    print("Pick an option")
    return input()


def tones_menu():
    print("Tones Menu")
    print("1 -> Ringing Tone")
    print("2 -> Ringing Volume")
    print("3 -> Incoming Call alert")
    print("4 -> Composer")
    print("5 -> Message alert tone")
    print("6 -> Keypad tones")
    print("7 -> Warning and game tones")
    print("8 -> Vibrating alert")
    print("9 -> Screen saver")
    print("B -> Back")
    print("Press an option")
    return input()


def settings_menu():
    print("Settings Menu")
    print("1 -> Call setting")
    print("2 -> Phone setting")
    print("3 -> Security setting")
    print("4 -> Restore factory setting")
    print("B -> Back")
    print("Pick an option to continue")
    return input()


def call_setting_menu():
    print("Call Setting Menu")
    print("1 -> Automatic redial")
    print("2 -> Speed dialling")
    print("3 -> Call waiting options")
    print("4 -> Phone line in use")
    print("5 -> Automatic answer")
    print("B -> Back")
    print("Pick an option to continue")
    return input()


def speed_dialing_menu():
    print("Speed Dialing Menu")
    print("1 -> Language")
    print("2 -> Cell info display")
    print("3 -> Welcome note")
    print("4 -> Network selection")
    print("5 -> Lights")
    print("6 -> Confirm SIM service actions")
    print("B -> Back")
    print("Pick an option to continue")
    return input()


def security_setting_menu():
    print("Security Setting Menu")
    print("1 -> PIN Code request")
    print("2 -> Call barring service")
    print("3 -> Fixed dialling")
    print("4 -> Closed user group")
    print("5 -> Phone security")
    print("6 -> Change access codes")
    print("B -> Back")
    print("Pick an option to continue")
    return input()


def clock_menu():
    print("Clock Menu")
    print("1 -> Alarm Clock")
    print("2 -> Clock Setting")
    print("3 -> Date setting")
    print("4 -> Stopwatch")
    print("5 -> Countdown timer")
    print("6 -> Auto update of date and time")
    print("B -> Back")
    print("Enter a number to get started")
    return input()


current_menu = display_menu()

while True:
    if current_menu == "1":
        current_menu = phonebook_menu()
        if current_menu == "8":
            current_menu = phonebook_options_menu()
            if current_menu == "B":
                current_menu = phonebook_menu()
        elif current_menu == "B":
            current_menu = display_menu()
    elif current_menu == "2":
        current_menu = messages_menu()
        if current_menu == "7":
            current_menu = message_settings_menu()
            if current_menu == "2":
                current_menu = message_settings_common_menu()
                if current_menu == "B":
                    current_menu = message_settings_menu()
            elif current_menu == "B":
                current_menu = messages_menu()
        elif current_menu == "B":
            current_menu = display_menu()
    elif current_menu == "4":
        current_menu = call_register_menu()
        if current_menu == "5":
            current_menu = call_duration_menu()
            if current_menu == "B":
                current_menu = call_register_menu()
        elif current_menu == "6":
            current_menu = call_cost_menu()
            if current_menu == "B":
                current_menu = call_register_menu()
        elif current_menu == "B":
            current_menu = display_menu()
    elif current_menu == "5":
        current_menu = tones_menu()
        if current_menu == "B":
            current_menu = display_menu()
    elif current_menu == "6":
        current_menu = settings_menu()
        if
