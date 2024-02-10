# Для простых задач с одной кучей
from functools import lru_cache

def moves(h): # тут записываем все варианты ходов через запятую
    if h % 2 == 0:
        return h + 1, h * 1.5
    else:
        return h + 1, h * 2

@lru_cache()
def game(h):
    if h >= 84: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1' # Петя выиграет первым ходом
    if all(game(m) == 'P1' for m in moves(h)): return 'B1' # Петя выиграет первым ходом
    if any(game(m) == 'B1' for m in moves(h)): return 'P2' # Петя выиграет вторым ходом
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2' # Ваня выиграет вторым ходом

for s in range(1, 84):
    if game(s) == 'B2': # здесь указываем, чей выигрыш нам нужно получить
        print(s)
