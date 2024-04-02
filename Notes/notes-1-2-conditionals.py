# Conditionals
# Author: Vincent Chen
# 15/02/24

# Implement the flowchart from notes

x= 100_000_000
y = -5

# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")

if x < y:
    print("X is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


foo = input("enter a number") # string

if int(foo) < -1 or int(foo) == 0:
    print("foo is less than or")
    print("or it's equal to zero")

# check is foo is inside the range
# greater than one and less than 1000

if foo > 1 and foo < 1000:
    print("Foo is in the range 2-999")
else:
    print("Foo is outside the range of 2-999")