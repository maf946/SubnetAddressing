def numberOfHostsRemaining(count, numOfBitsNeed, intNumOfPossibleHosts):
    totalSpaceNeeded = 2 ** numOfBitsNeed
    numHostsRemaining = intNumOfPossibleHosts - (int(count) + totalSpaceNeeded)
    print("You have " + str(numHostsRemaining) + " hosts remaining")
    return numHostsRemaining