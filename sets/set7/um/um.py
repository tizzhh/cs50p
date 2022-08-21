import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if count := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(count)

if __name__ == "__main__":
    main()