# All in one
# Vincent Chen
# March 5 2024

import random
import time

a = ["ace", 
    "two", 
    "three", 
    "four", 
    "five", 
    "six", 
    "seven", 
    "eight", 
    "nine", 
    "ten", 
    "jack", 
    "queen", 
    "king"
    ]

aa = ["ace", 
    "two", 
    "three", 
    "four", 
    "five", 
    "six", 
    "seven", 
    "eight", 
    "nine", 
    "ten", 
    "jack", 
    "queen", 
    "king"
]

b = [
    "of clubs",
    "of diamonds",
    "of hearts",
    "of spades",
    ]

bb = [
    "of clubs",
    "of diamonds",
    "of hearts",
    "of spades",
    ]
def main():
    u1 = int(c1)



def card(c1):
    c1 = random.randrange(1,14)

    if c1 == 1:
        int(c1)
        print("ace")
        return c1
    





c = input("Hello, would you like to play a quick game of black jack with me?")
if c.strip().lower() == "no":
    print("Ok, see you next time!")
elif c.strip().lower() == "yes":
    print("Wonderful, ")
    print("Your cards are:")
    time.sleep(.5)
    print(random.choice(a),random.choice(b), "and", random.choice(aa), random.choice(bb))
    time.sleep(.5)
    print("What would you like to do now?")

else:
    print("Sorry, I don't understand")
