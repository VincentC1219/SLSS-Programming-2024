# Work replace
# Vincent Chen
# 27/02/24

# create a function called translater
#   Accepts a string
#   Replace all hundreds with 💯 and noodles to 🍜
#   Return return


# Create a function called main
#   Propt user to type something
#   Use the translate on user input
#   Print the result



a = input("Type 100 and/or noodles").strip("!?,.").lower()

def emoji(a):
    a
    if a in ["100", "a hundred", "hundred"]:
        return "💯"
    if a == "noodles":
        return "🍜"
    if a in ["100 noodles", "100noodles", "a hundred noodles", "ahundrednoodles"]:
        return "💯🍜"


print(emoji(a))