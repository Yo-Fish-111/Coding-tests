def primecheck(maxprime): # function to check input is prime
    numtocheck = maxprime  # stores input to be used later
    prime = 0 # value mantains if a number is prime
    factors = [] # the factors of the input

    for i in range(2, int(round(numtocheck ** (1 / 2) + 2))): # runs through every value up to the square root of the input
        if maxprime % i == 0: # checks if this input is a factor of the input
            prime = 1 # updates the prime status of the input (or keeps it the same)
            maxprime = maxprime // i # it changes the value it is checking so it can find the prime factorisation
            factors.append(i) # adds the factor to the list
            i = i - 1 # reduces the potential factor so if the input is 4, for example, it will display both 2s
            #except it doesn't work

    if prime == 0: # if the prime status was never updated it will inform the user the number is prime
        return str(numtocheck) + " is prime"
    else: # if not it tells the user the factos
        return str(numtocheck) + " is not prime here are its prime factors: " + str(factors)


while True:
     print(primecheck(int(input("Please enter a number to check: ")))) # calls the function