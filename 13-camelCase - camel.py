camel_case = input("camelCase: ")
snake_case = ""

for x in camel_case:
    if x.isupper():
        snake_case = snake_case + "_" + x.lower()
    else:
        snake_case = snake_case + x

print("snake_case:", snake_case)
