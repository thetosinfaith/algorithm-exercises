from enum import Enum


class DisplayDateAndTime(Enum):
    MONDAY = "2014 - 07 - 05 14:34:14"
    TUESDAY = "2014 - 07 - 06"
    WEDNESDAY = "2014 - 07 - 07"
    THURSDAY = "2014 - 07 - 08"
    FRIDAY = "2014 - 07 - 09"
    SATURDAY = "2014 - 07 - 10"
    SUNDAY = "2014 - 07 - 11"


today = DisplayDateAndTime.MONDAY
if today == DisplayDateAndTime.MONDAY:
    print("2014 - 07 - 05 14:34:14")

