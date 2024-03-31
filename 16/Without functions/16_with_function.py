# If you have a task, where recursion limit is very huge, use this code

from functools import *

@cache
def f(n):
    if n < 3:
        return 3
    else:
        return 2 * n + 5 + f(n - 2)

for i in range(3028):
    f(i)

print(f(3027) - f(3023))
