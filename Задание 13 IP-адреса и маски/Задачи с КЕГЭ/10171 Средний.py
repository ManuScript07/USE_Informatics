from ipaddress import *

for mask in range(33):
    net = ip_network(f'115.53.128.88/{mask}', 0)
    print(net, net.num_addresses, net.netmask)

##115.53.128.0/17 32768 255.255.128.0
##115.53.128.0/18 16384 255.255.192.0
##115.53.128.0/19 8192 255.255.224.0
##115.53.128.0/20 4096 255.255.240.0
##115.53.128.0/21 2048 255.255.248.0
##115.53.128.0/22 1024 255.255.252.0

# 6
