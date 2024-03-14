from ipaddress import *
cnt = 0
for A in range(256):
    flag = 1
    n = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    for ip in n:
        if (f'{ip:b}'[16:]).count('1') <= 3:
            flag = 0
            break
    if flag == 0: continue
    else:
        print(A)
        break