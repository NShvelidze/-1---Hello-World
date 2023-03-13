import re
name = input("What's is your name? ")
nationality = input("Where are you from? ")

nationality = re.sub(" +", "",nationality)
nationality = nationality.capitalize()
nationality = nationality.strip()

name = re.sub(" +", "",name)
name = name.capitalize()
name = name.strip()

if nationality == "Georgia":
    greetings = "გამარჯობა"

elif nationality =="France":
    greetings = "Bonjour"

elif nationality =="Spain":
    greetings = "Hola"

elif nationality =="Italy":
    greetings = "Salve"
else:
    greetings = "Hello"

print(greetings + " " + name)
