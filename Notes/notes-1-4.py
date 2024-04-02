# Print Hello

def say_hello():
    Print("hello!")

say_hello 


# Create a function called say_hello_params
# Print "hello {Para,eter}"
# ---> e.g. say_hello_params("Jim")
#               Print "Hello Jim!"

def say_hello_params(name):
    Print(f"Hello {name}")



# def how_big(num):
#     if num < 0:
#         return "Very small"
#     if num < 10:
#         return "Pretty small"
#     if num < 30:
#         return "Not small"

# print(how_big(1))

# how_big(-1)


# result = how_big(1_000_000)
# print(result)

# Create a function called adder
#   Accepts two inputs that are numbers
#   Return the sum of both numbers

# def adder(x: int, y: int):
#     return x + y

# result = adder (1,1)