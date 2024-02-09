# Для простых задач с одной кучей
from functools import lru_cache

def moves(h):
    if h % 2 == 0:
        return h + 1, h * 1.5
    else:
        return h + 1, h * 2

@lru_cache()
def game(h):
    if h >= 84: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'

for s in range(1, 84):
    if game(s) == 'B2':
        print(s)
