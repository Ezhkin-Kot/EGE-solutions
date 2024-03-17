f = open('26_ege2022_day1.txt')
n = int(f.readline())
boxes = [int(x) for x in f.readlines()]
boxes.sort(reverse = True)
gift = [boxes[0]]
for i in range(1, n):
    if gift[-1] - boxes[i] >= 3:
        gift.append(boxes[i])
print('Количество:', len(gift))
print('Сторона маленькой коробки:', min(gift))