f = open("27-B.txt")
n = int(f.readline())
allNumbers = [int(x) for x in f.readlines()]  # input numbers
finalArr0 = [0] * 11  # remainder with three equal to 0
finalArr1 = [0] * 11  # remainder with three equal to 1
finalArr2 = [0] * 11  # remainder with three equal to 2

for i in allNumbers:
    countDegree = 0
    # count max degree of two
    while i % (2**(countDegree + 1)) == 0:
        countDegree += 1
        if countDegree == 10:
            break
    # find a remainder with three
    if i % 3 == 0:
        finalArr0[countDegree] += 1
    elif i % 3 == 1:
        finalArr1[countDegree] += 1
    else:
        finalArr2[countDegree] += 1

ans = 0
# find value with remainder of zero
for i in range(11):
    j = 10 - i
    ans += (finalArr0[i] * sum(finalArr0[max(i + 1, j):]))

for i in range(5, 11):
    ans += finalArr0[i] * (finalArr0[i] - 1) // 2

# find count of values with remainders two and one
for i in range(11):
    j = 10 - i
    ans += (finalArr1[i] * sum(finalArr2[j:]))

print(ans)