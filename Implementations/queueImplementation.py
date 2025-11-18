def declareQueue(desiredLength, dataType="CHAR"):
    global queue
    if dataType.upper() == "INT":
        queue = [i for i in range(desiredLength)]
    if dataType.upper() == "CHAR":
        queue = [f"{i}" for i in range(desiredLength)]
    if dataType.upper() == "BOOL":
        queue = [False for i in range(desiredLength)]
    if dataType.upper() == "FLOAT":
        queue = [i/(1) for i in range(desiredLength)]
    if dataType.upper() == "LIST":
        queue = [[i, i+1] for i in range(desiredLength)]
    else:
        queue = ["" for i in range(desiredLength)]
    nextAdress = 0
    return [queue, nextAdress]

def isEmpty(queue):
    return queue[1] == 0

def isFull(queue):
    return queue[1] == len(queue[0])

def retrieve(queue):
    if isEmpty(queue):
        return
    else:
        returnValue = queue[0][0]
        queue[1]-=1
        queue[0] = queue[0][1:]
        queue[0].append(returnValue)
        return returnValue

def add(queue, item):
    if isFull(queue):
        print("queue is Full")
        return MemoryError
    queue[0][queue[1]] = item
    queue[1]+=1

def peak(queue):
    if isEmpty(queue):
        print("queue is empty")
        return MemoryError
    return queue[0][0]

def displayQueue(queue):
    if isEmpty(queue):
        print("Queue is empty")
        return MemoryError
    returnQueue = [queue[0][i] for i in range(queue[1])]
    while len(returnQueue) != len(queue[0]):
        returnQueue.append("")
    return returnQueue

