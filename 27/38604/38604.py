f = open("27_B.txt")
n = int(f.readline())
allNumbers = [int(x) for x in f.readlines()]
narastItog = [0]
remainders = [0]
remaindersRev = []

for i in allNumbers:
    temp = (narastItog[-1] + i)
    narastItog.append(temp)
    remainders.append(temp % 43)

remaindersRev = remainders.copy()
remaindersRev.reverse()
maxSum = 0
for i in range(43):
    if remainders.count(i) > 0:
        temp = remaindersRev.index(i)
        a = remainders.index(i)
        if maxSum < (narastItog[len(remainders) - temp - 1] - narastItog[a]):
            maxSum = narastItog[len(remainders) - temp - 1] - narastItog[a]
            print(len(remainders) - temp - 1 - a)