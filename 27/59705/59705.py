f = open("27_B.txt")
k = int(f.readline())
n = int(f.readline())

allNumbers = [int(x) for x in f.readlines()]
summ = 30_000_000
currentMin1 = 10_000_000
minSum12 = 20_000_000
for i in range(n-2*k):
    currentMin1 = min(currentMin1, allNumbers[i])
    minSum12 = min(minSum12, currentMin1 + allNumbers[i+k])
    summ = min(summ, minSum12 + allNumbers[i + 2*k])

print(summ)