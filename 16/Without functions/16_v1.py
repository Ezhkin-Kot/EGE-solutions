f = [0] * 3028
for n in range(1, 3028):
    if n < 3: f[n] = 3
    else: f[n] = 2 * n + 5 + f[n-2]
print(f[3027] - f[3023])