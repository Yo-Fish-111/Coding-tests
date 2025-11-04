import os
if not os.path.exists("C:\\OMathData"):
    os.makedirs("C:\\OMathData")
    print("Created OMathData folder")

if os.path.isfile("C:\\OMathData\\primes.txt") == False:
    Primes = open("C:\\OMathData\\primes.txt", 'w')
    Primes.write("2\n3\n")
    Primes.close()
    print("Created primes text file")
inPrimes = open("C:\\OMathData\\primes.txt", 'r')
line = inPrimes.readline().strip()
Plist = []

while line != "":
    Plist.append(int(line))
    line = inPrimes.readline().strip()

inPrimes.close()

def primecheck(prime, Primelist):
    outPrimes = open("C:\\OMathData\\primes.txt", 'a')
    for i in range(Primelist[-1], prime+1, 2):
        append = True
        for j in Primelist:
            if i % j == 0:
                append = False
        if append:
            Primelist.append(i)
            Plist.append(i)
            outPrimes.write(str(i)+"\n")
    outPrimes.close()

    if Primelist[-1] == prime:
        return True
    else:
        return False



while True:
    possibleP = int(input("Please enter a number to check: "))
    if Plist[-1] == possibleP:
        print(f"{possibleP} is prime")
    elif Plist[-1] < possibleP:
        isPrime = primecheck(possibleP, Plist)
        if isPrime:
            print(f"{possibleP} is prime")
        else:
            print(f"{possibleP} is not prime")
    elif Plist[-1] > possibleP:
        if possibleP in Plist:
            print(f"{possibleP} is prime")
        else:
            print(f"{possibleP} is not prime")
