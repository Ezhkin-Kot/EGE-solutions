f = open("27-B.txt")
n = int(f.readline())
allNumbers = [int(x) for x in f.readlines()]
# Обычный одномерный список будет использоваться в качестве двумерного массива
# Для определения индекса будем переводить в десятичную систему
arr = [0] * 80
count = 0

for i in allNumbers[14:]:
    ost8 = i % 8
    del3 = 0
    while i % 3**(del3 + 1) == 0:
        del3 += 1
        if del3 == 9:
            break
    arr[ost8*10 + del3] += 1

for i in range(n-14):
    x = allNumbers[i]
    ost8 = x % 8
    del3 = 0
    while x % 3 ** (del3 + 1) == 0:
        del3 += 1
        if del3 == 9:
            break
    for j in range(9-del3, 10):
        count += arr[((8-ost8) % 8) * 10 + j]
    x = allNumbers[i + 14]
    ost8 = x % 8
    del3 = 0
    while x % 3 ** (del3 + 1) == 0:
        del3 += 1
        if del3 == 9:
            break
    arr[ost8 * 10 + del3] -= 1

print(count)