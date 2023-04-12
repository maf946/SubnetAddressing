def numberOfHostsRemaining(count, numOfBitsNeed):
    totalSpaceNeeded = 2 ** numOfBitsNeed
    numHostsRemaining = (int(count) - totalSpaceNeeded)
    print("You have " + str(numHostsRemaining) + " hosts remaining")
    return numHostsRemaining
