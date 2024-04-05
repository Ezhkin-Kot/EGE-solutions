from ipaddress import *
net = ip_network('203.111.195.0/255.255.240.0', 0)
cnt = 0
for ip in net:
    if (f'{ip:b}'.count('0')) % 3 == 0 and '111' in f'{ip:b}' and '000' in f'{ip:b}':
        cnt += 1
print(cnt)