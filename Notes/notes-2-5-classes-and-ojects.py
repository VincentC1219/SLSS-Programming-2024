# Classes and Objects
# Vicnent Chen
# 15/04/24


# Big ideas:
#   - Classes llow us to couple data and functions
# Objects are the ACTUAL representation of the class

# Create a pokemon calss; this represents a pokemon
class Pokemon: # use a capital letter for class names
    def __init__(self):
        """A special method (funtction) called a contrustor. Contains all the properties/variables"""
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
    def __init__(self,name="Pikachu"):
        # call constructor of parent class
        super().__init__()

        #Assign the default values to properties
        self.name = name
        self.id = 25
        self.type = "Electric"
        self.actual_cry = "Pikachu"
    def thundershock(self, defender: Pokemon) -> str:
        """Similate a thundershock attack aginst another Pokemon
        
        params:
            - defender: defending Pokemon
        
        Returns:
            str respresenting result of Pokemon"""

        if defender.type.lower() in ["water", "flying"]:
            response = response + "It was super effective."

        return response

#Change some properties in pokemon_one
#   Change its name
pokemon1 = Pokemon()

pokemon1.name = "Pikachu"
print(pokemon1.name)

pokemon1.id = 25
pokemon1.type = "Electric"

print(pokemon1.id)
print(pokemon1.type)

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

pokemon1.actual_cry = "Pikachu"
pokemon2.actual_cry = "Vaporeon"

print(pokemon1.cry())
print(pokemon2.cry())


# Test eat method
print(pokemon1.eat("berry"))
print(pokemon1.eat("potion"))
print(pokemon1.eat("poison")) # Mr. Ubial condones this very much

pikachu1 = Pikachu()
pikachu2 = Pikachu("speedy")

print(pikachu1.name) 
print(pikachu2.name)
print(pikachu1.cry())
print(pikachu2.eat("potion"))

print(pikachu1.thundershock(pokemon1))
print(pikachu2.thundershock(pokemon2))