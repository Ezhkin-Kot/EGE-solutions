f = open('26_L1__3yqpm.txt')
k = int(f.readline())
n = int(f.readline())

buyers = []
for i in f.readlines():
    buyers.append([int(x) for x in i.split()])
buyers = sorted(buyers)

cam = [-1] * n
leave = 0
cht = 0
last = 999
for buyer in buyers:
    for i in range(n):
        if cam[i] < buyer[0]:
            cam[i] = buyer[1]
            if (i + 1) % 2 == 0: cht += 1
            last = i + 1
            break
    else: leave += 1
print(cht, last)
