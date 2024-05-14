f = open("107_27_B.txt")
n = int(f.readline())
allBins = [int(x) for x in f.readlines()] * 2

summ64 = 0
for i in range(n):
    summ64 += allBins[i] * abs(n//2 - 1 - i)

leftSumm = sum(allBins[:n//2-1])
rightSumm = sum(allBins[n//2:n])

summ = summ64
sumMin = summ64
for i in range(n//2, n//2+n):
    summ += leftSumm + allBins[i-1]
    summ -= rightSumm
    leftSumm += allBins[i-1]
    leftSumm -= allBins[i-n//2]
    rightSumm -= allBins[i]
    rightSumm += allBins[i+n//2]
    sumMin = min(sumMin, summ)

print(sumMin * 3)


# Test for file A
minSumm = 1000000000
for i in range(65, 130 + 65):
    summ = 0
    for j in range(130):
        summ += allBins[i + j - 65] * abs(65 - j)
    minSumm = min(minSumm, summ)

print(minSumm*3)
