import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
figlet.getFonts()


try:
    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        text = input("input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(text))

    elif len(sys.argv) == 1:
        text = input("input: ")
        random_font = random.choice(figlet.getFonts())
        print(figlet.renderText(text))
    else:
        sys.exit()
except:
    print("Ivnalid usage")
    sys.exit()
