months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if date[0].isdigit() and date[1] == "/" or date[2] == "/":
        date = date.strip().split("/")
        while int(date[0]) > 12 or int(date[1]) > 31:
            date = input("Date: ").split("/")
        print (f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")
        break

    else:
        while not "," in date:
            date = input("Date: ")
        date = date.replace(",", " ")
        date = date.split()
        while not date[0] in months or int(date[1]) > 31 or date[0].isdigit():
            date = input("Date: ").replace(",", " ").split()
        print (f"{date[2]}-{int(months.index(str(date[0])))+1:02}-{int(date[1]):02}")
        break
