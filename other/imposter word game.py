from random import *

inNouns = open("C:\\data\\noun list.txt","r")
line = inNouns.readline()
nouns = []
while line != "":
    nouns.append(line)
    line = inNouns.readline()

numberOfPlayers = int(input("Please enter the number of players: "))

if randint(0,int(numberOfPlayers * 2.5)) == numberOfPlayers:
    numberOfImposters = randint(int(numberOfPlayers*0.5),numberOfPlayers)
elif randint(0, numberOfPlayers * 2) == numberOfPlayers:
    numberOfImposters = randint(int(numberOfPlayers * 0.2), int(numberOfPlayers*0.5))
else:
    numberOfImposters = 1

order = []
for i in range(numberOfPlayers-numberOfImposters):
    order.append(0)
for i in range(numberOfImposters):
    order.append(1)

shuffle(order)
word = nouns[randint(0,len(nouns))]
for i in range(numberOfPlayers):
    input("Press ENTER to show the word")
    if order[i] == 0:
        print(f"The word is {word}")
    elif order[i] == 1:
        print(f"You do not know the word you are the imposter")
    input("Press ENTER to hide the word")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

