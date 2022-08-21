import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"^.+https?://(?:www\.)?youtube\.com/embed/(\w+)", s)
    if match:
        return "https://youtu.be/" + match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()