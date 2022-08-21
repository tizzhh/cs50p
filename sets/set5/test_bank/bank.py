def main():
    a = input("Greeting: ")
    print(f"${value(a)}")


def value(greeting):
    greeting = greeting.lower()
    greeting = greeting.split()[0]
    greeting = greeting.replace(",", "")
    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()