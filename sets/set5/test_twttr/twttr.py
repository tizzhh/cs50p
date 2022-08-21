def main():
    a = input("Input: ").strip()
    print(shorten(a))

def shorten(word):
    j = 0
    remove = "aeiou"
    while True:
        check = False
        for i in range(j, len(word) - 1):
            if word[i].lower() in remove:
                word = word.replace(word[i], "")
                j = i
                check = True
                break
        if check == False:
            return word


if __name__ == "__main__":
    main()
