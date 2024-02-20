s = open('24.txt').readline().split('E')
cnt = 0
mx = 1000000000
for i in range(len(s)-99):
    for ii in range(i, i + 99):
        cnt += len(s[ii])
    mx = min(mx, cnt + 100)
    cnt = 0
print(mx)
