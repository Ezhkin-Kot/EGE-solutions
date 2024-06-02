from functools import *
@lru_cache(None)
def f(a, b):
  if a + b >= 47: return 0
  t = [f(a + 1, b), f(a * 2, b), f(a, b + 1), f(a, b * 2)]
  n = [i for i in t if i <= 0]
  if n: return -max(n) + 1
  else: return -max(t)
    
h = # В значение h ставим, чей ход выигрышный. Отрицательные - ходы Вани
# "1" - первый ход Пети; "-1" - первый ход Вани; "2" - второй ход Пети; "-2" - второй ход Вани и т.д.
for i in range(1, 43):
  if f(4, i) == h: print(i) 
