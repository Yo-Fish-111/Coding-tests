def declareStack(desiredLength, dataType="CHAR"):
    global stack
    if dataType.upper() == "INT":
        stack = [i for i in range(desiredLength)]
    if dataType.upper() == "CHAR":
        stack = [f"{i}" for i in range(desiredLength)]
    if dataType.upper() == "BOOL":
        stack = [False for i in range(desiredLength)]
    if dataType.upper() == "FLOAT":
        stack = [i/(1) for i in range(desiredLength)]
    if dataType.upper() == "LIST":
        stack = [[i, i+1] for i in range(desiredLength)]
    else:
        stack = ["" for i in range(desiredLength)]
    topPointer = -1
    bottomPointer = 0
    return [stack, bottomPointer, topPointer]

def isEmpty(stack):
    return stack[2] == -1

def isFull(stack):
    return stack[2] == len(stack[0])-1

def pop(stack):
    if isEmpty(stack):
        return
    else:
        returnValue = stack[0][stack[2]]
        stack[2]-=1
        return returnValue

def push(stack, item):
    if isFull(stack):
        print("Stack is Full")
        return MemoryError
    stack[2]+=1
    stack[0][stack[2]] = item

def peak(stack):
    if isEmpty(stack):
        print("Stack is empty")
        return MemoryError
    return stack[0][stack[2]]

def displayStack(stack):
    if isEmpty(stack):
        print("Stack is empty")
        return MemoryError
    returnStack = [stack[0][i] for i in range(stack[2]+1)]
    while len(returnStack) != len(stack[0]):
        returnStack.append("")
    return returnStack









