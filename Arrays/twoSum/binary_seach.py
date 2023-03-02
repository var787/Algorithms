# here we will set up two pointers and use a While-loop and binary search
# O(nLog(n)) time | O(n) space
def twoNumberSum(array, targetSum):
    # first we sort the array in ascending order so we can have a time complexity of O(nLog(n)) # noqa
    array.sort()
    # set up the two pointers to the start end of the array
    left = 0
    right = len(array) - 1
    # perform a while loop to add them both as long as left element is smaller than the right element # noqa
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
