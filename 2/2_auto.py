from itertools import *
def f1(w, x, y, z):
    return (w == x) and (y <= z)
def f2(w, x, y, z):
    return (w <= x) <= (y == z)
for a1, a2, a3, a4, f in product([0, 1], repeat = 5):
    t = [(1, a2, 1, 1), (a1, 1, 0, 0), (a1, 0, 0, a4)]
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if [f1(**dict(zip(p, r))) for r in t] == [1, 1, 0] and \
                    [f2(**dict(zip(p, r))) for r in t] == [0, f, 0]:
                print(p)