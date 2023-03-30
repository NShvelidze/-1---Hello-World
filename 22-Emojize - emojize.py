emoji_dict = {
    ":Christmas_tree:" : "🎄",
    ":OK_button:" : "🆗",
    ":angry_face:" : "😠",
    ":avocado:" : "🥑"
}

greetings = input("Input: ").replace(",","")
greetings = greetings.split(" ")

for emoji in greetings:
    if emoji in emoji_dict:
        emoji = emoji_dict[emoji]
    print(emoji, end = " ")
print("")
