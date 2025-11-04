from random import randint
tape = []

for i in range(15):
    tape.append(randint(0,1))
print(f"The start tape is {tape}")

codeSate = []
desiredStates = int(input("Enter the number of desired states: "))
for i in range(desiredStates-1):
    codeSate.append([[randint(0,1), randint(0,1), randint(-1,desiredStates-1)], [randint(0,1), randint(0,1), randint(0,desiredStates-1)]])
print(codeSate)
state = 0
position = int(len(tape)/2)
step = 0

while state != -1 and step < len(tape)-5:
    value = tape[position]
    tape[position] = codeSate[state][value][0]
    if codeSate[state][value][1] == 1:
        position = position + 1
    else:
        position = position - 1
    state = codeSate[state][value][2]
    print(tape)
    step = step + 1

print(tape)
print(codeSate)
print(step)

