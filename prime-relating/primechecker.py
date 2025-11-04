def primecheck(maxPrime):
    numtocheck = maxPrime
    i = 2
    prime = 0
    factors = []
    if maxPrime == 1:
        return "what, mate 1 isn't either prime or not"
    if maxPrime == 2:
        return "2 is prime"
    while True:
        if maxPrime % i == 0:
            prime = 1
            maxPrime = maxPrime // i

            factors.append(i)
            i = i - 1
        i = i + 1

        if i >= numtocheck//2 + 2:
            if prime == 0:
                return str(numtocheck) + " is prime"
            else:
                return str(numtocheck) + " is not prime here are its prime factors: " + str(factors)


while True:
     print(primecheck(int(input("Please enter a number to check: "))))