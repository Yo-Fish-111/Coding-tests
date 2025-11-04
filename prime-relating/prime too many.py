from functions import *

input = int(input("Please enter an integer to check: "))
check = checkPrime(input)

if not check:
    print(f"{input} is not prime")
else:
    print(f"{input} is prime")



