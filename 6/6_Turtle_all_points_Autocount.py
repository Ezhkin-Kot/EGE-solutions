from turtle import *

left(90)
ZOOM = 25
tracer(0)
begin_fill()

for _ in range(16):
    left(36)
    forward(4 * ZOOM)
    left(36)
end_fill()
up()

cnt = 0
canvas = getcanvas()
for x in range(-50, 50):
    for y in range(-50, 50):
        item = canvas.find_overlapping(x * ZOOM, y * ZOOM, x * ZOOM, y * ZOOM)
        if len(item) == 1 and item[0] == 5:
            cnt += 1

print(cnt)
done()
