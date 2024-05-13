from functools import *
def moves(h):
    a, b = h
    return (a + 3, b), (a * 2, b), (a, b + 3), (a, b * 2)
@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 300: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1' # any если ход Пети неудачный
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'
    if any(game(m) == 'B2' for m in moves(h)): return 'P3'
    if all(game(m) == 'P1' or game(m) == 'P2' or game(m) == 'P3' for m in moves(h)): return 'B3'
for s in range(1, 280):
    h = 20, s
    if game(h) == 'P3':
        print(s, game(h))
