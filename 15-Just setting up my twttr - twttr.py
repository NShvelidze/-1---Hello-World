word = input("write full word: ")
vowels = ["A", "E", "I", "O", "U"]

for x in word:
    if x.upper() in vowels:
        word = word.replace(x,"")
print(word)
