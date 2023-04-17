import string
import random
import ipaddress
import math
from ipaddress import IPv4Address
from random import getrandbits

boolPublicIPType = True  # True for a public IP address; False if you want a private IP address
intSubnetCount = 2
intPrefix = 24  # How large do you want the prefix to be? Enter an integer between 1 and 27, or anything else for random
boolRandomSubnetSizes = True  # True for randomly generated; False for manual

def generateIPAddress(boolPublicIPType):
    if (boolPublicIPType == False):
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
        addr = IPv4Address(getrandbits(32))
        while True:
            if(addr.is_global):
                break
        return addr

class Subnet:
    def __init__(self, name, prefixSize):
        self.name = name
        self.prefixSize = prefixSize
        self.numOfPossibleHosts = (2 ** (32 - self.prefixSize)) - 2
    def __str__(self):
        returnString = self.name
        returnString += "\n\tPrefix: " + str(self.prefixSize)
        returnString += "\n\tPossible Hosts: " + str(self.numOfPossibleHosts)
        return returnString

class Network:
    def __init__(self, IP_Address, intPrefix):
        self.subnets = []
        self.IP_Address = IP_Address
        self.intPrefix = intPrefix
    def __str__(self):
        return str(self.IP_Address) + "/" + str(self.intPrefix)

myNetwork = Network(generateIPAddress(boolPublicIPType), intPrefix)

for subnetCreatedCount in range(1, intSubnetCount + 1):
    subnetLetter = list(string.ascii_uppercase)[subnetCreatedCount - 1]
    intPrefix = random.randint(1, 27)
    myNetwork.subnets.append(Subnet("Subnet " + subnetLetter, intPrefix))


print(myNetwork)

for subnet in myNetwork.subnets:
    print(subnet)