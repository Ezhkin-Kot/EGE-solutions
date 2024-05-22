from fnmatch import *
def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
t = []
for i in range(10, 100):
    if f(i):
        t.append(i)
res = []
for i in range(10**6):
    if fnmatch(str(i), '1*1'):
        for j in t:
            for k in t:
                n = int(str(j) + str(i) + str(k))
                if n <= 10**10:
                    res.append(n)

print(len(set(res)))