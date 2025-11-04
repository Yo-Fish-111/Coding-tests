import random

answers = []

for i in range(0, 10):
    j = random.randint(50,255) # generates number
    print(f"{i}. {"{:08b}".format(j)}") # prints number in binary with question number
    answers.append(j)


input("press enter for answers") # holds until user input
print(answers) # prints answers

answers = []
time.sleep(4)

for i in range(0, 10):
    j = random.randint(50,255) # generates number
    print(f"{i}. {j}") # prints number in denary with question number
    answers.append("{:08b}".format(j))

input("press enter for answers") # holds until user input
print(answers) # prints answers



