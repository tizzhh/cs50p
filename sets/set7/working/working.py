import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    if match := re.search(r"^([0-9]+):?([0-9]+)? (\w+) (.+) ([0-9]+):?([0-9]+)? (\w+)$", s):
        hours1, mins1, format1, to, hours2, mins2, format2 = match.groups()
    else:
        raise ValueError

    if mins1 == None:
        mins1 = 0
    else:
        mins1 = int(mins1)
    if mins2 == None:
        mins2 = 0
    else:
        mins2 = int(mins2)
    hours1 = int(hours1)
    hours2 = int(hours2)

    if hours1 > 12 or hours1 < 1 or hours2 > 12 or hours2 < 1:
        raise ValueError
    if mins1 > 59 or mins1 < 0 or mins2 > 59 or mins2 < 0:
        raise ValueError
    if to != "to":
        raise ValueError
    if format1 != "AM" and format1 != "PM" or format2 != "AM" and format2 != "PM":
        raise ValueError

    if format1 == "AM" and format2 == "PM":
        if hours1 == 12:
            hours1 = 0
        if hours2 != 12:
            hours2 += 12
        return f"{hours1:02}:{mins1:02} to {hours2:02}:{mins2:02}"
    else:
        if hours1 != 12:
            hours1 += 12
        if hours2 == 12:
            hours2 = 0
        return f"{hours1:02}:{mins1:02} to {hours2:02}:{mins2:02}"

if __name__ == "__main__":
    main()