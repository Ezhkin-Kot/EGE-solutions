# One neep code for 20'th task USE (United State Exame, most knowed as ЕГЭ)
def f(x, h):
    if h == 3 and x >= 68: 
        return 1 # Победа
    if h == 3 and x < 68:
        return 0 # Поражение
    if x >= 68 and h < 3:
        return 0 # Поражение
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
            # Winner
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)
            # Looser
 
for x in range(1, 68):
    if f(x, 0) == 1:
        print(x)