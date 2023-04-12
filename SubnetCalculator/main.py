import ipaddress
import math
import random
from generateIPAddress import generateIPAddress
from numberOfHostsRemaining import numberOfHostsRemaining
from manGenSubSize import manGenSubSize

#Options
boolPublicIPType = False # True for a public IP address; False if you want a private IP address
intSubnetCount = 3 # 2 for 2 subnets, 3 for 3
intPrefix = 23  # How large do you want the prefix to be?  (1-27, or -1 for random)
boolRandomSubnetSizes = True # false to set subnet sizes manually; true if you want them randomly generated


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
        count = 0
        count = numberOfHostsRemaining(count, numOfBitsNeed, intNumOfPossibleHosts)
        thisDict["B"] = input("Enter the size of subnet B: ")
        numOfBitsRaw = math.log2(int(thisDict["B"]) + 2)
        numOfBitsNeed = math.ceil(numOfBitsRaw)
        if(intSubnetCount == 3):
            count = numberOfHostsRemaining(count, numOfBitsNeed, intNumOfPossibleHosts)
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
print(str(thisDict["A"]) + " hosts                     " + str(thisDict["B"]) + " hosts")
if(intSubnetCount == 3):
    print("                  C               ")
    print("              " + str(thisDict["C"]) + " hosts")

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
