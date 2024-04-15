# Две кучи
def f(x, y, p, n):
    if x >= 21 or y >= 21: return p % 2 == n % 2
    if p == n: return 0
    h = [f(x + 3, y, p + 1, n), f(x * 2, y, p + 1, n), f(x, y + 3, p + 1, n), f(x, y * 2, p + 1, n)]
    return any(h) if (p + 1) % 2 == n % 2 else all(h)
for s in range(1, 21):
    for n in range(1, 7): # Количество ходов
        if f(4, s, 0, n):
            print(s, n)
            break