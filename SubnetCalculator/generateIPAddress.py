import ipaddress
from ipaddress import IPv4Network, IPv4Address
from random import getrandbits
def generateIPAddress(boolPublicIPType):
    if (boolPublicIPType == False):
        print("Private address: ", end='')
        while True:
            addr = ipaddress.IPv4Address(getrandbits(32))
            if (addr.is_private):
                octets = addr.exploded.split(".")
                if (octets[0] == "10"):
                    break
                elif (octets[0] == "172"):
                    if (octets[1] >= "16" and octets[1] <= "31"):
                        break
                elif (octets[0] == "192"):
                    if (octets[1] == "168"):
                        break
        return addr

    else:
        print("Public address: ", end='')
        addr = IPv4Address(getrandbits(32))
        while True:
            if(addr.is_global):
                break
        return addr