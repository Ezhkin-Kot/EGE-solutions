f = [3, 3]
x = 0
y = 0
for n in range(3, 3028):
    f.append(2 * n + 5 + f[0])
    if n == 3027: x = f[2]
    if n == 3023: y = f[2]
    f.pop(0)
print(x - y)