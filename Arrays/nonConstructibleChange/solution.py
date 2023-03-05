
# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):
    # first sort all elements in array in an ascending order
    coins.sort()
    # initialize a variable, set to 0, that keeps track of the change being created # noqa
    currentCreatedChange = 0
    # loop
    for coin in coins:
        # here we check to see if the next coin/element is greater that the currentCreated Change + 1 because if it is than we would consider (currentCreatedChange + 1) to be the minimum change we can create. # noqa
        #The reason for that is as we keep adding the elements to the previously created change, if the created change + 1 exceeds the next element then it would not be possible for us make the change between the two adjacent elements # noqa
        if coin > currentCreatedChange + 1:
            return currentCreatedChange + 1
        currentCreatedChange += 1
    return currentCreatedChange + 1
