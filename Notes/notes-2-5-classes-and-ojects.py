# Classes and Objects
# Vicnent Chen
# 15/04/24


# Big ideas:
#   - Classes llow us to couple data and functions
# Objects are the ACTUAL representation of the class

# Create a pokemon calss; this represents a pokemon
class Pokemon: # use a capital letter for class names
    def __init_(self):
        """A special method (funtction) called a contrustor. Contains all the properties/"""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"

        print("A new pokemon is born")

        # Create two Pokemon using our class
        # Make one pokemon that is pikachu

pokemon_one = Pokemon()

#Change some properties in pokemon_one
#   Change its name

pokemon_one.name = "Pikachu"
print(pokemon_one.name)

pokemon_one.id = 25
pokemon_one.type = "Electric"

print(pokemon_one.id)
print(pokemon_one.type)

pokemon2 = Pokemon()

pokemon2.name = "Vaporeon"
pokemon2.id = 134
pokemon2.type = "Water"
pokemon2.weight = 29.0
pokemon2.height = 1.0

print(pokemon2)