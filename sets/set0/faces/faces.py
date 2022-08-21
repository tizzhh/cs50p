def main():
    a = input()
    convert(a)

def convert(a):
    a = a.replace(":(", "🙁")
    print(a.replace(":)", "🙂"))

if __name__ == "__main__":
    main()