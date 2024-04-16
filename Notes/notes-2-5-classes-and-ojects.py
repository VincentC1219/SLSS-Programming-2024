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
        self.actual_cry = "roar"

        print("A new pokemon is born")

        # Create two Pokemon using our class
        # Make one pokemon that is pikachu
def cry(self) -> str:
    """represents the sound a pokemon makes
    
    returns:
        - string representing the sound it makes"""
    return f'{self.name} says, "{self.actual_cry}"!'
pokemon_one = Pokemon

def eat(self, food:str) -> str:
    """Represents feeding the Pokemon
    
    Params:
        - food: what food you feed it
        
    Returns:
        - What it says after eating it"""
    if food.lower() == "berry":
        return f"{self.name} ate the berry and says \"TUM!\""
    elif food.lower() == "potion":
        return f"{self.name} consumed the potion and feels healthier"
    elif food.lower == "poison":
        return f"{self.name} ate the poison and begins to colapse \n {self.name} feels uneasy and begins to squint their eyes \n {self.name} as fainted"
    else:
        return f"{self.name} batted the {food} away."
    
# Create a new child class of Pokemon
class Pikachu(Pokemon):
    def __init__(self):
        # call constructor of parent class
        super().__init__()

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

print(pokemon2.name)
print(pokemon2.id)
print(pokemon2.type)
print(pokemon2.weight)
print(pokemon2.height)

pokemon_one.actual_cry = "Pikachu"
pokemon2.actual_cry = "Vaporeon"

print(pokemon_one.cry())
print(pokemon2.cry())


# Test eat method
print(pokemon_one.eat("berry"))
print(pokemon_one.eat("potion"))
print(pokemon_one.eat("poison")) # Mr. Ubial condones this very much