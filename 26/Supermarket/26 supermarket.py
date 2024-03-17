f = open('26_ege2022_day2.txt')
n = int(f.readline())
purchases = [int(x) for x in f.readlines()]
summ = sum(purchases)
purchases.sort(reverse = True)
print('Предполагал заплатить:', (summ - (sum(purchases[:n // 4]) // 2)))
purchases.sort()
print('Заплатил:             ', (summ - (sum(purchases[:n // 4]) // 2)))