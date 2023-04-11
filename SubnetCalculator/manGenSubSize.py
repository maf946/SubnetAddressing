import math

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

