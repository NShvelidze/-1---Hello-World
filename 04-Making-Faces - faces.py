def convert(x):
    if x == "hello :)":
        return "hello 🙂"
    elif x == "goodbye :(":
        return "goodbye 🙁"
    elif x == "Hello :) Goodbye :(":
        return "Hello 🙂 Goodbye 🙁"
    else:
        return "Write correct emoticons"

greetings1 = convert(str(input("greetings: ")))

print(greetings1)
