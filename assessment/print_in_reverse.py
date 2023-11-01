from typing import Type

first_name = (input("What's your first name?"))
last_name = (input("What's your last name?"))


class String:
    pass


reversed = Type[String] = list[first_name, last_name]

for reversed in range(0, len(reversed)):
    print(reversed)
