fruits = {"apple": 130, "avocado" : 50, "banana": 110, "cantaloupe": 50,
          "grapefruit": 60, "grapes": 90, "kiwifruit": 90, }

item = input("Item: ")

if item in fruits:
    print("Calories:", fruits[item])
