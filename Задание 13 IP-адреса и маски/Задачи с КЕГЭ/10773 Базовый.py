from ipaddress import *


for mask in range(33):
    net = ip_network(f'133.57.64.130/{mask}', 0)
    print(net)
##133.57.64.0/18
##133.57.64.0/19
##133.57.64.0/20
##133.57.64.0/21
##133.57.64.0/22
##133.57.64.0/23
##133.57.64.0/24
# 7 
