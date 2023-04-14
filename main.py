# Created by Garrett Ongie (gqo5049@psu.edu)

import ipaddress
import math
import random
from ipaddress import IPv4Network, IPv4Address
from random import getrandbits


#Options - IST 220 students: experiment with these values!
boolPublicIPType = True # True for a public IP address; False if you want a private IP address
intSubnetCount = 3 # 2 for 2 subnets, 3 for 3
intPrefix = 24  # How large do you want the prefix to be? Enter an integer between 1 and 27, or anything else for random
if ((isinstance(intPrefix, int)) != True):
    intPrefix = -1
boolRandomSubnetSizes = True # True for randomly generated; False for manual

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

def manGenSubSize(intSubnetCount, thisDict, intNumOfPossibleHosts, boolRandomSubnetSizes):
    # For A
    subnetAAddressesNeededA = int(thisDict["A"]) + 2
    numberOfBitsRawA = math.log2(subnetAAddressesNeededA)
    numberOfBitsNeededA = math.ceil(numberOfBitsRawA)
    # For B
    subnetAAddressesNeededB = int(thisDict["B"]) + 2
    numberOfBitsRawB = math.log2(subnetAAddressesNeededB)
    numberOfBitsNeededB = math.ceil(numberOfBitsRawB)

    # Calculate number of bits needed
    addresssesAssignedA = 2 ** numberOfBitsNeededA
    addresssesAssignedB = 2 ** numberOfBitsNeededB

    totalAddresses = addresssesAssignedA + addresssesAssignedB

    if (intSubnetCount == 3):
        # For C
        subnetAAddressesNeededC = int(thisDict["C"]) + 2
        numberOfBitsRawC = math.log2(subnetAAddressesNeededC)
        numberOfBitsNeededC = math.ceil(numberOfBitsRawC)
        addresssesAssignedC = 2 ** numberOfBitsNeededC
        totalAddresses = addresssesAssignedA + addresssesAssignedB + addresssesAssignedC

    if (int(totalAddresses) < intNumOfPossibleHosts):
        #First check for duplicates
        if(thisDict["A"] == thisDict["B"]):
            if (boolRandomSubnetSizes == False):
                print("\nContains duplicates, try again")
            if(intSubnetCount == 3):
                return -1, numberOfBitsNeededA, numberOfBitsNeededB, numberOfBitsNeededC
            return -1, numberOfBitsNeededA, numberOfBitsNeededB
        if(intSubnetCount == 3):
            if (thisDict["A"] == thisDict["C"] or thisDict["B"] == thisDict["C"]):
                if (boolRandomSubnetSizes == False):
                    print("\nContains duplicates, try again")
                return -1, numberOfBitsNeededA, numberOfBitsNeededB, numberOfBitsNeededC


        #Print subnet information
        print(
            "\nSubnet A has {} hosts, so it will need at least {} addresses (for the subnet ID and broadcast address).".format(
                int(thisDict["A"]), subnetAAddressesNeededA))
        print("The smallest number of bits that satisfy this is {}.".format(numberOfBitsNeededA))
        print("This is because log₂({}) = {}, which rounds up to {} bits.".format(
            subnetAAddressesNeededA, numberOfBitsRawA, numberOfBitsNeededA))

        print(
            "\nSubnet B has {} hosts, so it will need at least {} addresses (for the subnet ID and broadcast address).".format(
                int(thisDict["B"]), subnetAAddressesNeededB))
        print("The smallest number of bits that satisfy this is {}.".format(numberOfBitsNeededB))
        print("This is because log₂({}) = {}, which rounds up to {} bits.".format(
            subnetAAddressesNeededB,
            numberOfBitsRawB,
            numberOfBitsNeededB))
        if(intSubnetCount == 3):
            print(
                "\nSubnet C has {} hosts, so it will need at least {} addresses (for the subnet ID and broadcast address).".format(
                    int(thisDict["C"]), subnetAAddressesNeededC))
            print("The smallest number of bits that satisfy this is {}.".format(numberOfBitsNeededC))
            print("This is because log₂({}) = {}, which rounds up to {} bits.".format(
                subnetAAddressesNeededC,
                numberOfBitsRawC,
                numberOfBitsNeededC))
            return 1, numberOfBitsNeededA, numberOfBitsNeededB, numberOfBitsNeededC
        return 1, numberOfBitsNeededA, numberOfBitsNeededB
    else:
        if(boolRandomSubnetSizes == False):
            print("\nToo large, try again")
        if(intSubnetCount == 3):
            return -1, numberOfBitsNeededA, numberOfBitsNeededB, numberOfBitsNeededC
        else:
            return -1, numberOfBitsNeededA, numberOfBitsNeededB

def numberOfHostsRemaining(count, numOfBitsNeed):
    totalSpaceNeeded = 2 ** numOfBitsNeed
    numHostsRemaining = (int(count) - totalSpaceNeeded)
    print("You have " + str(numHostsRemaining) + " hosts remaining")
    return numHostsRemaining

##Start of Program
#Part 1- Private or Public IP generation

addr = generateIPAddress(boolPublicIPType)
print(addr)

#Part 2- Number of Subnets
#creates placeholder values for subnet sizes
if (intSubnetCount == 3):
    thisDict = {
        "A": 1,
        "B": 2,
        "C": 3
    }
else:
    thisDict = {
        "A": 1,
        "B": 2
    }
    intSubnetCount = "2"

#Part 3- Prefix Size

if not (intPrefix >= 1 and intPrefix <= 27):
    intPrefix = random.randint(1, 27)
    print("The random prefix is: " + str(intPrefix))


#Part 4- Number of Possible Hosts
intNumOfPossibleHosts = (2 ** (32 - intPrefix)) - 2
print("With a prefix of " + str(intPrefix) + ", the maximum possible number of hosts is: " + str(intNumOfPossibleHosts))

#Part 5- Subnet Sizes

#Manually generate size for subnets
if(boolRandomSubnetSizes == False):
    while True:
        print()
        thisDict["A"] = input("Enter the size of subnet A: ")
        numOfBitsRaw = math.log2(int(thisDict["A"]) + 2)
        numOfBitsNeed = math.ceil(numOfBitsRaw)
        count = intNumOfPossibleHosts
        count = numberOfHostsRemaining(count, numOfBitsNeed)
        thisDict["B"] = input("Enter the size of subnet B: ")
        numOfBitsRaw = math.log2(int(thisDict["B"]) + 2)
        numOfBitsNeed = math.ceil(numOfBitsRaw)
        if(intSubnetCount == 3):
            count = numberOfHostsRemaining(count, numOfBitsNeed)
            thisDict["C"] = input("Enter the size of subnet C: ")

        #convert values to integers
        thisDict = {key: int(value) for key, value in thisDict.items()}
        # Move them to a list so we can sort it more easily
        dictValues = list(thisDict.values())
        dictValues.sort(reverse=True)
        # Add them back to the dictionary
        thisDict["A"] = dictValues[0]
        thisDict["B"] = dictValues[1]
        if (intSubnetCount == 3):
            thisDict["C"] = dictValues[2]
            val, numberOfBitsNeededA, numberOfBitsNeededB, numberOfBitsNeededC = manGenSubSize(intSubnetCount, thisDict, intNumOfPossibleHosts, boolRandomSubnetSizes)
        else:
            #Checks if the subnet meets our requirements
            val, numberOfBitsNeededA, numberOfBitsNeededB = manGenSubSize(intSubnetCount, thisDict, intNumOfPossibleHosts, boolRandomSubnetSizes)
        if(val == 1):
            break

#Randomly generate size for subnets
else:
    while True:
        # not ideal but it just keep running the loop until it finds an instance where it is the correct size
        thisDict["A"] = random.randint(1, intNumOfPossibleHosts)
        thisDict["B"] = random.randint(1, intNumOfPossibleHosts)
        if (intSubnetCount == 3):
            thisDict["C"] = random.randint(1, intNumOfPossibleHosts)

        # Sort them
        dictValues = list(thisDict.values())
        dictValues.sort(reverse=True)
        # Add them back to the dictionary
        thisDict["A"] = dictValues[0]
        thisDict["B"] = dictValues[1]
        if (intSubnetCount == 3):
            thisDict["C"] = dictValues[2]
            val, numberOfBitsNeededA, numberOfBitsNeededB, numberOfBitsNeededC = manGenSubSize(intSubnetCount,
                                                                                               thisDict,
                                                                                               intNumOfPossibleHosts,
                                                                                               boolRandomSubnetSizes)
        else:
            # Checks if the subnet meets our requirements
            val, numberOfBitsNeededA, numberOfBitsNeededB = manGenSubSize(intSubnetCount, thisDict, intNumOfPossibleHosts,
                                                                                               boolRandomSubnetSizes)
        if (val == 1):
            break

#Part 6- Printing the Subnet
octets = addr.exploded.split(".")
print("\nPutting hosts in descending order...\n\n       Example Subnet Addressing")
print("            " + octets[0] + "." + octets[1] + "." + octets[2] + ".0/" + str(intPrefix))
print("    A                            B")
print("🖥️"+ str(thisDict["A"]) + " hosts                     🖥️" +  str(thisDict["B"]) + " hosts")
if(intSubnetCount == 3):
    print("                  C               ")
    if(thisDict["C"] == 1):
        print("              🖥️" + str(thisDict["C"]) + " host")
    else:
        print("              🖥️" + str(thisDict["C"]) + " hosts")

#Part 7
print("\nCIDR Notation:")
address = str(octets[0] + "." + octets[1] + "." + octets[2] + ".0")
ip_address = ipaddress.IPv4Address(address)
subnetA = ipaddress.IPv4Network((ip_address, (32 - numberOfBitsNeededA)), strict=False)
print(f"Subnet A: {subnetA}")
print(f"Broadcast address: {subnetA.broadcast_address}")
print(f"First IP of the Subnet A: {subnetA.network_address + 1}")
print(f"Last IP of the Subnet A: {subnetA.broadcast_address - 1}")


ip_addressB = ipaddress.IPv4Address(subnetA.broadcast_address + 1)
subnetB = ipaddress.IPv4Network((ip_addressB, (32 - numberOfBitsNeededB)), strict=False)
print(f"\nSubnet B: {subnetB}")
print(f"Broadcast address: {subnetB.broadcast_address}")
print(f"First IP of the Subnet B: {subnetB.network_address + 1}")
print(f"Last IP of the Subnet B: {subnetB.broadcast_address - 1}")


if(intSubnetCount == 3):
    ip_addressC = ipaddress.IPv4Address(subnetB.broadcast_address + 1)
    subnetC = ipaddress.IPv4Network((ip_addressC, (32 - numberOfBitsNeededC)), strict=False)
    print(f"\nSubnet C: {subnetC}")
    print(f"Broadcast address: {subnetC.broadcast_address}")
    print(f"First IP of the Subnet C: {subnetC.network_address + 1}")
    print(f"Last IP of the Subnet C: {subnetC.broadcast_address - 1}")
