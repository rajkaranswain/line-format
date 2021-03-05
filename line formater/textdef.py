def lineformater(phrase):
    intro = ("who","why","why","how")
    if phrase.startswith(intro):
        return f"{phrase.capitalize()}?"
    else :
        return f"{phrase.capitalize()}." 
fineline = []
while True:
    user_input = input("say to format")
    if user_input == "\end":
        break
    else:
        fineline.append(lineformater(user_input))

print(" ".join(fineline))           