import re

text = input("Write your Text: ")
text = re.sub(" +","...",text)

print(text)
