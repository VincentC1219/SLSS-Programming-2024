# Mc Donut
# vicnent Chen
# 22/02/24


#Ask about their mc order

print("...")
ans1 = input("would you like fries with yout order?")

# Fries
if ans1.strip().lower() == "yes":
    ans2 = input("Ok, would you like medium, small or large?")
    if ans2.lower().strip() == "medium":
        print("ok, I can add medium fries to your order")
    elif ans2.lower().strip() == "small":
        print("Ok, I can add small fries to your order")
    elif ans.lower().strip() == "large":
        print("Ok, I'll add lare fries to your order")
    else:
        print(f"{ans2}? I'm sorry I don't quite understand")
    ans3 = input("Ok, you total will come up to be 25.83. would you like to tip?")
elif ans1.strip().lower() == "no":
    ans3 = input("Ok, then will your total will come down to $19.76. Would you like to tip?")
else:
    print(f"{ans1}? I'm sorry but I don't understand")

# Tipping
if ans3.strip().lower() == "no":
    print("I'm sorry, but tipping in mandatory, I'll add a twenty five percent tip to your order. That you for your kindness")
elif ans3.strip().lower() == "yes":
    print("Wonderful, thank you very much for the tip")