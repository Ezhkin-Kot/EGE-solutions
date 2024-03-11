f = open("/Users/sergejdarin/Downloads/26.txt")
n = int(f.readline())
allClients = []

for i in f.readlines():
    allClients.append([int(x) for x in i.split()])

allClients = sorted(allClients)

window1 = []
window2 = []
countWindow2 = 0
countWindow1 = 0
countLeft = 0

for client in allClients:
    if len(window1) > 1:
        while window1[1] <= client[0]:
            window1.pop(1)
    if len(window2) > 1:
        while window2[1] <= client[0]:
            window2.pop(1)

    if ((len(window1) <= len(window2)) and (client[2] == 0)) or (client[2] == 1):
        if len(window1) == 0:
            window1.append(client[0] + client[1])
            countWindow1 += 1
        elif len(window1) < 15:
            window1.append(window1[-1] + client[1])
            countWindow1 += 1
        else:
            countLeft += 1
    else:
        if len(window2) == 0:
            window2.append(client[0] + client[1])
            countWindow2 += 1
        elif len(window2) < 15:
            window2.append(window2[-1] + client[1])
            countWindow2 += 1
        else:
            countLeft += 1

print(countWindow2, countLeft)
print(countWindow1)