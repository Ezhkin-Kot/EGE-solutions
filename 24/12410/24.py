f = open('C:/Users/manul/Хлам/Файлы для инфы/24_12410.txt')
s = f.readline()
k = j = m = 0
for i in range(1, len(s)):
	if s[i] < s[i - 1]: k += 1
	while k > 100000:
		if s[j + 1] < s[j]: k -= 1
		j += 1
	if k == 100000:
		m = max(m, i - j + 1)
print(m)