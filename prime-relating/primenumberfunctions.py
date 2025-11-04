import time
def factorcheck(maxPrime):
    i = 2
    prime = 0
    factors = []
    if maxPrime < 0:
        maxPrime = maxPrime * -1
        factors.append(-1)
    numtocheck = maxPrime
    if maxPrime == 2:
        return 0

    while True:
        if maxPrime % i == 0:
            prime = 1
            maxPrime = maxPrime // i
            factors.append(i)
            i = i - 1
            if numtocheck > 50000000:
                print(i)

        i = i + 1

        if i >= numtocheck//2 + 2:
            if prime == 0:
                return 0
            else:
                return factors

def primeness(Prime):
    factors = factorfind(Prime)
    check = 0
    for j in range(len(factors)):
        check = check +  factors[j]
    check = check / (Prime+1)

    return check

def factorfind(Prime):
    i = 2
    factors = [1]
    if Prime < 0:
        Prime = Prime * -1
        factors = [-1, 1]
    numtocheck = Prime
    if Prime == 1:
        return [1]
    if Prime == 2:
        return [2, 1]
    while True:
        if Prime % i == 0:
            factors.append(i)
            if numtocheck > 50000000:
                print(i)

        i = i + 1

        if i >= numtocheck // 2 + 2:
            factors.append(numtocheck)
            return factors

def primecheck(maxPrime):
    if maxPrime < 0:
        maxPrime = maxPrime * -1
    if maxPrime == 2:
        return 0
    for i in range(2,maxPrime//2 + 2):
        if maxPrime % i == 0:
            return 1
    return 0


check = "RETURN" 
print("send the command 'RETURN' at any time to change the type of prime check\ntyping 'INFO' on mode select screen will output further info")
while True:
    print("0 for the prime factorisation\n1 to test if a number is prime\n2 to check the primeness of a number\n3 to find all factors of a number")
    checktype = input("select mode: " )
    while True:
        if checktype != "INFO" and checktype != "RETURN":
            check = input("Please enter a number to check: ")
            if check == "RETURN":
                break
            elif checktype == '0' or '1' or '2' or '3':
                checktype = int(checktype)
                if checktype == 0:
                    output = str(factorcheck(int(check)))
                    if output == "0":
                        print(str(check) + " is prime")
                    else:
                        print(str(check) + "'s prime factorisation is " + output)

                if checktype == 1:
                    output = primecheck(int(check))
                    if output == 0:
                        print(str(check) + " is prime")
                    if output == 1:
                        print(str(check) + " is not prime")

                if checktype == 2:
                    print(str(check) + " has a primeness of " + str(primeness(int(check))))

                if checktype == 3:
                    factors = factorfind(int(check))
                    print("the factors of " + str(check) + " are " + str(factors) + " thats " + str(len(factors)) + " factors")

        elif checktype == "INFO":
            print("==================================================================================================================================================================\n0 will find the prime factorisation of number (such that all output numbers are prime and multiplying them equals the input)\n1 will just output if a number is prime or not\n2 adds the all factors of a number and divides by the input + 1\n3 outputs all factors of number (above 50 million it will print factors as it goes)\nthis program, when given with a negative, number uses -1 as a factor (if applicable)\nand converts the number to its positive counterpart\nthis program often does not function with 0 or 1")
            print("this program was developed by YoFish\nand may never be updated\nall functions here are free to use\n==================================================================================================================================================================")
            time.sleep(5)
            break
        elif checktype == "RETURN":
            break
        elif checktype != '0' or '1' or '2' or '3':
            print("ERROR mode cannot be user input please try again")
            checktype = input("select mode: ")
