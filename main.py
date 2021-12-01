import math

def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def pickRandomIP():
    from random import choice
    ip = []
    for i in range(0,3):
        ip.append(choice([i for i in range(1,223)]))
    ip.append(0)
    hostBits = choice([i for i in range(23,26)])

    #debugging
    ip.clear()
    ip.append(33)
    ip.append(47)
    ip.append(110)
    ip.append(0)
    ip.append(25)

    ip.append(hostBits)
    return ip

def returnIP(ip):
    theIP = ("{}.{}.{}.{}/{}".format(ip[0], ip[1], ip[2], ip[3], ip[4]))
    return theIP

def pickRandomHostCounts(numberOfSubnets):
    from random import choice
    hostCounts = []
    for i in range(0, numberOfSubnets):
        hostCounts.append(choice([i for i in range(10, 150)]))
    return hostCounts

def printQuestion01(ip):
    print("\n## Question 1: Is the address space public or private?")
    private = False
    if (ip[0] == 10):
        private = True
    elif (ip[0] == 172 & ip[1] >=16 & ip[1] <= 31):
        private = True
    elif (ip[0] == 192 & ip[1] == 168):
        private = True

    if (private):
        print("\nThe address space is private, because it is in one of the three defined private IP address ranges")
    else:
        print("\nThe address space is public, beacuse it is not in one of the three defined private IP address ranges")

def printQuestion02(ip):
    print("\n## Question 2: How many hosts can there be in this address space?")
    hostBits = 32 - ip[4]
    numHosts = 2 ** hostBits - 2
    print("\nThe number of hosts is {}.".format(numHosts))
    print("The maximum number of hosts is always equal to 2ˣ - 2, which here evaluates to 2{} - 2 = {}".format(superscript(str(hostBits)), numHosts))
    print("x is determined by subtracting the number of subnet bits from 32, which here evalutes to 32 - {} = {}".format(ip[4], hostBits))
    print("\nThe reason we have to subtract 2 from the final number is because there are always 2 addresses allocated")
    print("for each address block: the subnet ID (the first address) and the broadcast address (the last address).")

def printQuestion03(ip, subnetAHostCount):
    print("\n## Question 3: What is the subnet address of subnet A? (CIDR notation)")
    subnetAAddressesNeeded = subnetAHostCount + 2
    print("\nSubnet A has {} hosts, so it will need at least {} addresses (for the subnet ID and broadcast address).".format(subnetAHostCount,subnetAAddressesNeeded ))
    numberOfBitsRaw = math.log2(subnetAAddressesNeeded)
    numberOfBitsNeeded = math.ceil(numberOfBitsRaw)
    print("The least number of bits that satisfy this is {}".format(numberOfBitsNeeded))
    print("\tThis is because log₂({}) = {}, which means we actually need {} bits.".format(subnetAAddressesNeeded, numberOfBitsRaw, numberOfBitsNeeded))

def printQuestion04(ip, subnetAHostCount):
    print("\n## Question 4: What is the broadcast address of subnet A?")
    subnetABroadcastAddress = 255
    print("\nThe broadcast address of subnet A ({}) is {}.{}.{}.{}/{}, because it is the last address in the IP range.".format(returnIP(ip), ip[0], ip[1], ip[2], subnetABroadcastAddress, ip[4]))

if __name__ == '__main__':
    ip = pickRandomIP()
    hostCounts = pickRandomHostCounts(2)
    subnetAHostCount = hostCounts[0]
    subnetBHostCount = hostCounts[1]
    print("Consider a router and two attached subnets, A and B.")
    print("Subnet A contains {} hosts.".format(subnetAHostCount))
    print("Subnet B contains {} hosts.".format(subnetBHostCount))
    ## TODO: don't always say 24
    print("The subnets share the 24 high-order bits of the address space: {}.{}.{}.{}/{}".format(ip[0], ip[1], ip[2], ip[3], ip[4]))
    print("Assign subnet addresses to each of the subnets(A and B) so that the amount of address space assigned is minimal, " +
    "\nand at the same time leaving the largest possible contiguous address space available for assignment if a new subnet were to be added.")
    printQuestion01(ip)
    printQuestion02(ip)
    printQuestion03(ip,subnetAHostCount)
    printQuestion04(ip, subnetAHostCount)



