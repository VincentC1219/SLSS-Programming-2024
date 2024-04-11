# Vincent Chen
# Mid term activity
# 9 April. 2024


import random
import time


# def num(start: str) -> int:
#     value = " "
#     if start == 0:
#         print("Sorry I can't count down from zero")
    
#     elif start < 0:
#         print(f"Sorry but I can't count down from negative numbers")
        
#     elif start > 0:
#         int(start)
#         return start

    
    

# def countdown(num):
#     for i in range(start):
#         print(num(num - 1))


    
# start = input("What number do you want me to count down from?")
# str(start)
# num(start)

# countdown(int(start))



def check(start):
    if start == 0:
        print("Sorry I can't countup from zero")
    elif start < 0:
        print("sorry, I can't countup from a negative number")
    elif start > 0:
        int(start)
        begin = start
        return begin
    
def countup(begin: str) -> int:
    int(begin)
    for i in range(begin):
        print(check(i + 1))
        time.sleep(.5)

start = check(int(input("Hello, please give me a number for me to count to towards \n")))
countup(start)