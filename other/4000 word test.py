from random import randint
alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphahigh = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

outFile = open("C:\\OMathData\\DyegoText.txt", "w")
capital = 0
comma = 4
commaNum = 0
for i in range(50000+randint(0,50)):

    for j in range(randint(2,7)):
        if (j == i and randint(0,20) == 19) or (capital == 0 and j == 0):
            outFile.write(alphahigh[randint(0, 25)])
            capital = 0
        else:
            outFile.write(alpha[randint(0,25)])
    capital +=1
    comma +=1
    chance = 10-capital + 3
    if chance < 1:
        chance = 1
    if randint(0, chance+commaNum) == 0 and capital > 4:
        outFile.write(",")
        comma = 0
        commaNum = commaNum * 2
        capital -=4
    if (randint(0, chance) == 0 and capital > 4 and comma > 4) or (commaNum > 5):
        outFile.write(".")
        capital = 0
        comma = 0
        commaNum = 1
    outFile.write(" ")


outFile.close()
