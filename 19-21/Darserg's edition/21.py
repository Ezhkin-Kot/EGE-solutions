# Two neeps code
def f(x, h):
    if (h == 2 or h == 4) and x >= 68:
        return 1 # Победа
    if h == 4 and x < 68:
        return 0 # Поражение
    if h < 4 and x >= 68:
        return 0 # Поражение
    else:
        if h % 2 == 1: # Проверка, чей сейчас ход
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1) # Если ход первого игрока (Пети), то нужно проверить его ходы на возможную победу
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1) # Иначе нужно проверить, что Ваня не может проиграть
    
    for x in range(1, 68):
        if f(x, 0) == 1:
            print(x)
            break

    