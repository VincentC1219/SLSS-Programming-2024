# Random
# Vincent Chen
# 12/03/24

import random
import time

choice = random.random()
if choice < .5:
    cat = "dead"
else:
    cat = "alive"

#-------------------------------

print("There is a cat in the box, in a room of poison")
time.sleep(.5)
print("The poison has a 50/50 chance of killing the cat")
time.sleep(.75)
print("Now, when we open the box, what do you think cat is?")
guess = input(" a) Dead \n b) Alive \n")

# Dead
while True:
    if guess.lower().strip() == "a":
        a = "dead"
        if a == cat:
            print("yes, the cat is dead")
            break
        else:
            print("No, the cat is very much alive")
            break
    elif guess.lower().strip() == "dead":
        if guess == cat:
            print("yes, the cat is dead")
            break
        else:
            print("No, the cat is very much alive")
            break

    # Alive

    elif guess.lower().strip() == "b":
        b = "alive"
        if b == cat:
            print("Correct, it is alive")
            break
        else:
            print("No, the cat is dead")
            break
    elif guess.lower().strip() == "alive":
        if guess == cat:
            print("Correct, it is alive")
            break
        else:
            print("No, the cat is dead")
            break

    else:
     print("This is for science, do you think the cat is:")
     guess = input(" a) Dead \n b) Alive \n")
    
    