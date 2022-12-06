import ipaddress
from random import getrandbits
from random import choice
import random
from ipaddress import IPv4Network, IPv4Address


# from netaddr import *
# import pprint
# def ip2bin(ip):
#     octets = map(int, ip.split('/')[0].split('.')) # '1.2.3.4'=>[1, 2, 3, 4]
#     binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
#     range = int(ip.split('/')[1]) if '/' in ip else None
#     return binary[:range] if range else binary
#
#
# addr = ipaddress.ip_address('192.0.2.1')
# print(ip2bin(str(addr)))
#
# exit()
#
#
# ip = IPNetwork('172.16.0.0/12')
# pp = pprint.PrettyPrinter()
# pp.pprint("ip.cidr = %s" % ip.cidr)
# pp.pprint("ip.first.ip = %s" % ip[0])
# pp.pprint("ip.last.ip = %s" % ip[-1])
#
# ## DEBUG
# exit()
# ## DEBUG


def printRow(label, value):
    print('{:<30s}{:<5s}'.format(label + ":", str(value)))

def returnIP(ip):
    theIP = ("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3]))
    return theIP


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # determine public or private
    publicOrPrivate = choice(range(0, 2))  # 0 means public, 1 means private



    ## DEBUG
    publicOrPrivate = 0

    if (publicOrPrivate == 0):
        # we want to pick a random public IP

        while True:
            addr = IPv4Address(getrandbits(32))
            if (addr.is_global):
                break


    ## code for public addresses
    else:
        # we want to pick a random private IP

        privateRangeFamily = choice(range(0, 3))

        match privateRangeFamily:
            case 0:
                printRow('Range', "Private (Class A)")
                subnet = IPv4Network('10.0.0.0/24')
            case 1:
                printRow('Range', "Private (Class B)")
                subnet = IPv4Network('172.16.0.0/12')
            case 2:
                printRow('Range', "Private (Class C)")
                subnet = IPv4Network('192.168.0.0/16')
            case _:
                print("Something weird has happened")

        bits = getrandbits(subnet.max_prefixlen - subnet.prefixlen)
        firstAddress = subnet[1]
        lastAddress = subnet[-2]

        addr = IPv4Address(subnet.network_address + bits)
        printRow('subnet.max_prefixlen', subnet.max_prefixlen)
        printRow('subnet.prefixlen', subnet.prefixlen)
        printRow('subnet.num_addresses', subnet.num_addresses)
        printRow('subnet.broadcast_address', subnet.broadcast_address)
        printRow('First address', firstAddress)
        printRow('Last address', lastAddress)
        printRow('Random address in range', str(addr))
        printRow('Beginning of next subnet', IPv4Address(lastAddress) + 2)