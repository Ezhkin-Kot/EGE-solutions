f = open('C:/Users/manul/Хлам/Файлы для инфы/24_11954.txt')
s = f.readline()
l = cnt = 0
cnt_min = 10 ** 10
for r in range(len(s)):
    if s[r] == 'Y':
        cnt = 0
        l = r + 1
    if s[r] == 'X': cnt += 1
    while cnt >= 500:
        cnt_min = min(cnt_min, r - l + 1)
        if s[l] == 'X': cnt -= 1
        l += 1
print(cnt_min)