def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    count = 0
    if len(s) > 6 or len(s) < 2:
        return False
    if s.isalpha():
        return True
    for i in range(len(s)):
        if s[i].isnumeric():
            start = i
            break
        else:
            count += 1
    if count >= 2 and s[start:len(s)].isnumeric() and int(s[start]) != 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()