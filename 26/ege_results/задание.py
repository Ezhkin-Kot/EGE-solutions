f = open("C://Users/Solaris/Downloads/26(1).txt")
countAb, countPlace = f.readline().split()
countPlace = int(countPlace)
docs = []
withoutDocs = []
for i in range(int(countAb)):
    temp = [int(x) for x in f.readline().split()]
    maxChoise = 0
    regular = 0
    if temp[0] == 1:
        regular = sum(temp[1:3])
        if len(temp) == 5:
            maxChoise = max(temp[-1], temp[-2])
        else:
            maxChoise = temp[-1]
        docs.append(maxChoise + regular)
    if temp[0] == 0:
        regular = sum(temp[1:3])
        if len(temp) == 5:
            maxChoise = max(temp[-1], temp[-2])
        else:
            maxChoise = temp[-1]
    withoutDocs.append(maxChoise + regular)

docs = sorted(docs, reverse=True)
withoutDocs = sorted(withoutDocs, reverse=True)

print(docs[countPlace-1]+1)
print(withoutDocs[countPlace-1])
