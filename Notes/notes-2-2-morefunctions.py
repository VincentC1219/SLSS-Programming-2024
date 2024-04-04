# More funcitons
# Vincent Chen
# April 4, 2024



def star(num_star: int) -> str:
    # Return given number of stars *****
    value = " "
    # if value == 0 or value == 1 "*"
    # if value > 1 "8" * mum_star
    # else negative number -> error
    if num_star == 0 or num_star == 1:
        value = "*"
    return value






# # multiply strings
# greeting = "Hello"
# print(greeting * 2)


# print("The quick brown fox jumped over the lazy dog. " * 2)

print(star(1))
print(star(100))
