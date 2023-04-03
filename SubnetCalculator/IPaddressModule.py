## this was me experimenting with the ipaddress module

import ipaddress
from random import getrandbits
from random import choice
import random
from ipaddress import IPv4Network, IPv4Address
from enum import Enum

def printRow(label, value):
    print('{:<30s}{:<5s}'.format(label + ":", str(value)))

def returnIP(ip):
    theIP = ("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3]))
    return theIP


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # determine public or private
    class AddressType(Enum):
        Public = 0
        Private = 1
    publicOrPrivate = choice(range(0, 2))  # 0 means public, 1 means private

    if (AddressType(publicOrPrivate).name) == "Public":
        # we want to pick a random public IP

        while True:
            addr = IPv4Address(getrandbits(32))
            if (addr.is_global):
                break
        print(addr)
    ## code for public addresses
    else:
        # we want to pick a random private IP
        privateRangeFamily = choice(range(0, 3))
        if (privateRangeFamily == 0):
                printRow('Range', "Private (Class A)")
                subnet = IPv4Network('10.0.0.0/24')
        elif (privateRangeFamily == 1):
            printRow('Range', "Private (Class B)")
            subnet = IPv4Network('172.16.0.0/12')
        elif (privateRangeFamily == 2):
            printRow('Range', "Private (Class C)")
            subnet = IPv4Network('192.168.0.0/16')
        else:
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