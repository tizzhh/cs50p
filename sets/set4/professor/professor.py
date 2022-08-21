import random

def main():
    score = 10
    n = get_level()
    for i in range(10):
        if not generate_integer(n):
            score -= 1
    print(score)


def get_level():
    while True:
        try:
            a = int(input("Level: "))
        except ValueError:
            pass
        else:
            while a != 1 and a != 2 and a != 3:
                a = int(input("Level: "))
            return a


def generate_integer(level):
    x = random.randint(0 if level == 1 else 10 ** (level - 1), (10 ** level) - 1)
    y = random.randint(0 if level == 1 else 10 ** (level - 1), (10 ** level) - 1)
    for i in range(3):
        print(f"{x} + {y} = ", end="")
        try:
            a = int(input())
        except ValueError:
            pass
        else:
            if a == x + y:
                return True
        print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False


if __name__ == "__main__":
    main()