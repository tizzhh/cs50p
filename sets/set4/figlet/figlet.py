import sys

from random import choice
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Invalid usage")

if len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")

if not sys.argv[2] in figlet.getFonts():
        sys.exit("Invalid usage")

a = input("Input: ").strip()

if len(sys.argv) == 1:
    figlet.setFont(font = choice(figlet.getFonts()))
    print(figlet.renderText(a))

if len(sys.argv) == 3:
    print(sys.argv[2])
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(a))
