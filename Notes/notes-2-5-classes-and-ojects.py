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
        self.weigt = 0
        self.height = 0
        self.type = "normal"

        print("A new pokemon is born")

        # Create two Pokemon using our class
        # Make one pokemon that is pikachu

pokemon_one = Pokemon()

#Change some properties in pokemon_one
#   Change its name
print(pokemon_one.name)
pokemon_one.name = "Pikachu"
print(pokemon_one.name)