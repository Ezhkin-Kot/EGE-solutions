from turtle import *
k = 20 # коэффициент масштаба
tracer(0) # убираем анимацию отрисовки
left(90) # направляем вдоль оси ординат (изначально направлена вдоль оси абсцисс)

# далее переписываем программу черепахи
pendown()
for i in range(2):
    forward(5 * k)
    left(90)
    back(13 * k)
    left(90)
penup()
back(10 * k)
right(90)
forward(9 * k)
left(90)
pendown()
for i in range(2):
    forward(11 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
# рисуем координатную сетку
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot(3)

done() # чтобы рисунок не закрылся автоматически после выполнения