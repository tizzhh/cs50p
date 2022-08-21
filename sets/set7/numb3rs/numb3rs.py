import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    if re.search(r"^([0-9]|[1-9][0-9]|[1-2][0-5][0-5])\.([0-9]|[1-9][0-9]|[1-2][0-5][0-5])\.([0-9]|[1-9][0-9]|[1-2][0-5][0-5])\.([0-9]|[1-9][0-9]|[1-2][0-5][0-5])$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()