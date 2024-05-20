f = open("/Users/sergejdarin/Downloads/107_27_B.txt")
n = int(f.readline())
minSum = 10 ** 20
allContainers = [int(x) for x in f.readlines()]
leftSum = allContainers[0]  # Points, which would cost more with every step
rightSum = 0  # Points, which would cost less with every step
cost = 0
for i in range(1, n//2 + 1):
    cost += allContainers[i] * i
    rightSum += allContainers[i]

for i in range(n//2 + 1, n):
    cost += allContainers[i] * (n - i)
    leftSum += allContainers[i]

for i in allContainers.copy():
    allContainers.append(i)

for i in range(1, n):
    cost += leftSum - rightSum
    rightSum += (allContainers[i + (n // 2)] - allContainers[i])
    leftSum += (allContainers[i] - allContainers[i + (n // 2)])
    minSum = min(minSum, cost)


print(minSum * 3)
