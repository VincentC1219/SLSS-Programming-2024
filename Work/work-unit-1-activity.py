# Unit 1 activity
# Vincent Chen
# March 5 2024

import time

start = input("Hello, I'm a calculator, please input two numebrs and I can either multiply, or divide numbers, what would you like for me to do?")
if start == "multiply":
    def main():
        a = a_to_float(input("What would your first number be?"))
        time.sleep(.5)
        b = b_to_float(input(f"What would you like to multiply {a} by?"))
        time.sleep(.5)
        c = float(a) * float(b)
        time.sleep(1)
        print(c)
    def a_to_float(aa):
       float(aa)
       return(aa)
    def b_to_float(bb):
        float(bb)
        return(bb)
    main()
elif start == "divide":
    def main():
        a = a_to_float(input("What would your first number be?"))
        time.sleep(.5)
        b = b_to_float(input(f"What would you like to multiply {a} by?"))
        time.sleep(.5)
        c = float(a) / float(b)
        time.sleep(1)
        print(c)
    def a_to_float(aa):
        float(aa)
        return(aa)
    def b_to_float(bb):
        float(bb)
        return(bb)
    main()
else:
    print("Sorry, I don't understand")

