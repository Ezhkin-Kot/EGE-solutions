f = open("27-B.txt")
n = int(f.readline())
allNumbers = [int(x) for x in f.readlines()]
arr = [[0] * 7 for _ in range(7)]

count = 0

for i in range(n):
    x = allNumbers[i]
    for j in range(7):
        count += arr[j][(i-x-j) % 7]
    arr[x % 7][i % 7] += 1

print(count)
