def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    hrs = float(time[0])
    if "a" in time[1]:
        mins = float(time[1].split(" ")[0])
        return hrs + mins / 60
    elif "p" in time[1]:
        mins = float(time[1].split(" ")[0])
        return hrs + 12 + mins / 60
    else:
        mins = time[1]
        mins = float(mins)
        return hrs + mins / 60

if __name__ == "__main__":
    main()