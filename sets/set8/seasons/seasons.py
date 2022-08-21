from datetime import datetime, date
import datetime
import sys, re
import inflect

inflector = inflect.engine()
def main():
    if match := re.search(r"^([1-2][0-9][0-9][0-9]-(?:[0][0-9]|[1][0-2])-(?:[0][0-9]|[1-2][0-9]|[3][0-1]))$", input("Date of Birth: ")):
        date1 = match.group()
    else:
        sys.exit("Invalid date")
    diff = convert(date1)
    print(inflector.number_to_words(diff, andword="").capitalize(), "minutes")

def convert(date1):
    today = date.today()
    today = datetime.datetime.combine(today, datetime.time(0,0))
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    diff = today - date1
    diff = int(diff.days)
    diff *= 24 * 60
    return diff

if __name__ == "__main__":
    main()