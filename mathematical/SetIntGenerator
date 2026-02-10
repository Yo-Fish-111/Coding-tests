def getIntSet(n):
    if n == 0:
        return "{}"
    if n == 1:
        return "{{}}"
    prevSet = getIntSet(n-1)
    return "{" + prevSet + "," + prevSet[1:-1] + "}"
four = getIntSet(4)
print(four)
