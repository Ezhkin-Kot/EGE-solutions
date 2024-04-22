def f(x, y, m):
    if x * y >= 385: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 5, y, m - 1), f(x * 2, y, m - 1), f(x, y + 5, m - 1), f(x, y * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h) #any/all если никто не поддаётся, если кто-то поддаётся - any\any
print('19:', [s for s in range(1, 55) if f(8, s, 2)]) # В переменную m пишем, чей ход выигрышный
print('20:', [s for s in range(1, 55) if not(f(8, s, 1)) and f(8, s, 3)]) # Дописываем условие, что Петя не может выиграть первым ходом
print('21:', [s for s in range(1, 55) if  not(f(8, s, 2)) and f(8, s, 4)]) # Аналогично дописываем, что Ваня не может выиграть первым ходом