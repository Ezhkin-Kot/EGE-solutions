#  Darserg's edition

f = open("24.txt").readline().split("E")
n = len(f)
minlen = 0
for i in f[:100]:
    minlen += len(i)
for i in range(1, n-100):
    count = 0
    for j in f[i:i+99]:
        count += len(j)
    minlen = min(minlen, count + 100)
print(minlen)
