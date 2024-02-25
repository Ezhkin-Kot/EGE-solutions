import math
f = open("27_B.txt")
n = int(f.readline())
allPoints = []


for x in f.readlines():
    temp = [int(x.split()[0]), int(x.split()[1])]
    allPoints.append(temp)

minSumm = 1000000000

leftSum = 0
rightSum = 0
countLeft = 0
countRight = 0
for i in range(1, n):
    lenOfRoad = (allPoints[i][0] - allPoints[0][0])
    k = math.ceil(allPoints[i][1] / 36)
    rightSum += lenOfRoad * k
    countRight += k

currentPrice = rightSum
print(currentPrice)
minPrice = currentPrice
for i in range(1, n):
    lenOfRoad = allPoints[i][0] - allPoints[i-1][0]
    countLeft += math.ceil(allPoints[i-1][1] / 36)
    leftSum += countLeft * lenOfRoad
    rightSum -= countRight * lenOfRoad
    countRight -= math.ceil(allPoints[i][1] / 36)
    currentPrice = leftSum + rightSum
    if minPrice > currentPrice:
        minPrice = currentPrice

print(minPrice, rightSum, countRight)