name = input("What's is your name? ")
name = name.strip()
name = name.capitalize()
import re
name = re.sub(" +", "", name)

print("Hello, " + name + " ,Nice to meet You!")
