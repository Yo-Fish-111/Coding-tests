import matplotlib.pyplot as plt

def primeness(Prime):
    factors = factorfind(Prime)
    check = 0
    for j in range(len(factors)):
        check = check +  factors[j]
    check = check / (Prime+1)
    return check

def factorfind(Prime):
    i = 2
    factors = [1]
    if Prime < 0:
        Prime = Prime * -1
        factors = [-1, 1]
    numtocheck = Prime
    if Prime == 1:
        return [1]
    if Prime == 2:
        return [2, 1]
    while True:
        if Prime % i == 0:
            factors.append(i)

        i = i + 1

        if i >= numtocheck // 2 + 2:
            factors.append(numtocheck)
            return factors
x = []
y = []
maxy = []
bigy = 0
maxx = []

for i in range(1, 90721):
    ifactors = len(factorfind(i))
    x.append(i)
    y.append(ifactors)

    if ifactors > bigy:
        maxy.append(ifactors)
        maxx.append(i)
        bigy = ifactors
        print(i)

print(x)
print(maxx)
print(y)
print(maxy)
fig, ax = plt.subplots()
ax.scatter(x, y, 1, [(0.82, 0.5, 0.4)])
ax.plot(maxx, maxy)
ax.text(len(x)/4,maxy[-1]*1.1,"Highly Composite Numbers")
plt.show()
 