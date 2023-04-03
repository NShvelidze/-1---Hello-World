import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
             continue
    except(ValueError):
         continue
    for i in range(level):
            i = random.randint(1,level)
    break

while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                 continue
        except(ValueError):
            continue
        if guess > i:
            print("Too Large")
        if guess < i:
            print("Too Small")
        if guess == i:
            print("Just right!")
            break
