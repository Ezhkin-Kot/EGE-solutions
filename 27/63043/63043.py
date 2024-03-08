f = open("27-B.txt")
k = int(f.readline())
n = int(f.readline())
allNumbers = [int(x) for x in f.readlines()]

summ12 = 0

for i in range(n-3*k):
    if summ12 <= allNumbers[i] + allNumbers[i + 3*k]:
        summ12 = allNumbers[i] + allNumbers[i + 3*k]
        a1 = allNumbers[i]
        a2 = allNumbers[i+3*k]
print(a1, a2, max(allNumbers))
print(summ12 + max(allNumbers))
