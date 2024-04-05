# Loops and integration
# Vincent Chen
# Apirl 5, 2024


# Print "something" 10 teimes

for _ in range(2):
    print("something")

# Create a grocery list
grocery_list = [
    "Potato",
    "Tomato",
    "Chlorine",
    "Rubbing alcohol",
    "hydrochloric acid",
    "baking soda",
    "sugar",
]

# for every item in lst:
#   * {item}
#   * {item}
#   * {item}

for item in grocery_list:
    # skip the rest of the list
    # if we get to hydrochloric acid
    if item.lower() == "hydrochloric acid":
        print("You shouldn't buy that")
        break
    print(f"* {item}")

# Can you count using a for loop?
# Use a loop to count to 100

for i in range(100):
    print(i + 1)

print("e")
