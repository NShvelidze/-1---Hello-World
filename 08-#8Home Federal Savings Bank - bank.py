greetings = input("greeting: ").title()

if greetings.startswith("Hello"):
    print("0$")
elif greetings.startswith("H"):
    print("20")
else:
    print("100$")
