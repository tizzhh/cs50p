import sys

from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")

if ".jpg" not in sys.argv[1].lower() and ".jpeg" not in sys.argv[1].lower() and ".png" not in sys.argv[1].lower():
    sys.exit("Invalid input")

if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(sys.argv[1]):
        pass
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
image = Image.open(sys.argv[1])
size = shirt.size
image = ImageOps.fit(image, size)

image.paste(shirt, shirt)

image.save(sys.argv[2])