f = open()
n = int(f.readline())
allContainers = [int(x) for x in f.readlines()]

allContainers = sorted(allContainers, reverse=True)

array = []
countIterations = 0

while len(allContainers) > 0:
    i = allContainers.pop(0)
    temp = [i]
    for j in allContainers:
        if i - j >= 7:  # Difference between last and current container
             i = j
            temp.append(allContainers.pop(allContainers.index(j)))
    array.append(temp)

maxLen = 0

for i in array:
    if len(i) > maxLen:
        maxLen = len(i)

print(len(array), maxLen)
