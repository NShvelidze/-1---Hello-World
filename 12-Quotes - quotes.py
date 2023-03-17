sequence =  [
    "These aren't the droids you're looking for.", # Obi-Wan Kenobi
    "It is hard to fail but it is worse never to have tried to succeed.", # Theodore Roosevelt
    "That which does not kill us makes us stronger.", # Friedrich Nietzsche
    "I have not failed. I've just found 10,000 ways that won't work.", # Thomas A. Edison
    "The future belongs to those who believe in the beauty of their dreams.", # Eleanor Roosevelt
]

quote = input("What is the quote? ")
author = input("Who said it? ").title()

if quote == sequence[0] and author == "Obi-Wan Kenobi":
    print(f"{author} says, \"{sequence[0]}\"")
elif quote == sequence[1] and author == "Theodore Roosevelt":
    print(f"{author} says, \"{sequence[1]}\"")
elif quote == sequence[2] and author == "Friderich Nietzsche":
    print(f"{author} says, \"{sequence[2]}\"")
elif quote == sequence[3] and author == "Thomas A. Edison":
    print(f"{author} saus, \"{sequence[3]}\"")
elif quote == sequence[4] and author == "Eleanor Roosevelt":
    print(f"{author} says, \"{sequence[4]}\"")
else:
    print("Wrong quote")
