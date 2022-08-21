a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

a = a.replace("-", " ").strip()

if a == "42" or a == "forty two":
    print("Yes")
else:
    print("No")
