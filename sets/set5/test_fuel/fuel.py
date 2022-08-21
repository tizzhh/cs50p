def main():
    a = input("Fraction: ")
    res = convert(a)
    print(f"{gauge(res)}")


def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            while x > y and y != 0:
                fraction = input("Fraction: ").split("/")
                x = int(fraction[0])
                y = int(fraction[1])
                return round(x/y*100)
            return round(x/y*100)
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
