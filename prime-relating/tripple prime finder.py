import os
if not os.path.exists("C:\\OMathData"):
    os.makedirs("C:\\OMathData")
    print("Created OMathData folder")

if os.path.isfile("C:\\OMathData\\primes.txt"):
    inPrimes = open("C:\\OMathData\\primes.txt", 'r')
    line = inPrimes.readline().strip()
    Plist = []

    while line != "":
        Plist.append(line)
        line = inPrimes.readline().strip()

    inPrimes.close()

else:
    print("Prime file does not exist please run the prime generator first")
    quit()

if not os.path.isfile("C:\\OMathData\\trippleprimes.txt"):
    Primes = open("C:\\OMathData\\trippleprimes.txt", 'w')
    Primes.write("")
    Primes.close()
    print("Created tripple primes text file")
inPrimes = open("C:\\OMathData\\trippleprimes.txt", 'r')
line = inPrimes.readline().strip()
Ptriplist = []

while line != "":
    Ptriplist.append(int(line))
    line = inPrimes.readline().strip()

inPrimes.close()

outPrimes = open("C:\\OMathData\\trippleprimes.txt", 'a')
for i in range(len(Ptriplist) + 1, len(Plist) - 1):
    if int(Plist[i]) + 2 == int(Plist[i+1]) and int(Plist[i]) + 4 == int(Plist[i+2]):
        Ptriplist.append(Plist[i])
        print(f"{Plist[i]}, {Plist[i+1]} and {Plist[i+2]} are tripple primes")
        outPrimes.write(str(Plist[i]) + "\n" + str(Plist[i+1])+ "\n" + str(Plist[i+2]))

outPrimes.close()