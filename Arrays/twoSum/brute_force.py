# Brute Force - Here we will use two for-loops to find the numbers.
# O(n^2) time | O(1) space
def twoNumberSum1(array, targetSum):
    # we loop through the array once and assign the first number.(Here we loop till the second last element in the array) # noqa
    for i in range(len(array) - 1):
        firstNum = array[i]
        # we loop through the array a second time starting from the second element and assign the second number.(Here we loop till the last element of the array ) # noqa
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            # we add both numbers and return them if they equal the target number # noqa
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    # if we don't get any matches, we return an empty array
    return []
