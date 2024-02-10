from fnmatch import *
for x in range(0, 10 ** 10, 2024):
    if fnmatch(str(x), '1?2*4'):
        if int(x ** 0.5) == (x ** 0.5):
            print(x, (x // 2024))