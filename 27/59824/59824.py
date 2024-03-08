f = open("27B_59824.txt")
n = int(f.readline())
k = int(f.readline())

allNumbers = [int(x) for x in f.readlines()]
narastItog = [allNumbers[0]]

for i in range(1, n):
    narastItog.append(narastItog[-1]+allNumbers[i])
summ = -9999999999
minPlace = 999999999999
for i in range(n-k):
    minPlace = min(minPlace, narastItog[i])
    summ = max(summ, narastItog[i+k]-minPlace)

print(summ)