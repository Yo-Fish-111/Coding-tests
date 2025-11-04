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

if not os.path.isfile("C:\\OMathData\\spacedtwinprimes.txt"):
    Primes = open("C:\\OMathData\\spacedtwinprimes.txt", 'w')
    Primes.write("3\n7\n")
    Primes.close()
    print("Created twin primes text file")
inPrimes = open("C:\\OMathData\\spacedtwinprimes.txt", 'r')
line = inPrimes.readline().strip()
Ptwinlist = []

while line != "":
    Ptwinlist.append(int(line))
    line = inPrimes.readline().strip()

inPrimes.close()

outPrimes = open("C:\\OMathData\\spacedtwinprimes.txt", 'a')
for i in range(len(Ptwinlist)+1, len(Plist)-1):
    if int(Plist[i]) + 4 == int(Plist[i+1]):
        Ptwinlist.append(Plist[i])
        print(f"{Plist[i]} and {Plist[i+1]} are spaced twin primes")
        outPrimes.write(str(Plist[i]) + "\n" + str(Plist[i+1])+ "\n")

outPrimes.close()