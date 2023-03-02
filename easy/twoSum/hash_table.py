# Here we will be using a dictionary/hash table to store elements and will compare against it
# O(n) time / O(n) space
def twoNumberSum(array, targetSum):
# Lets start with an empty dictionary to store the elements
    nums = {}
# A single for-loop for the list to find the difference between target number and element
    for num in array:
        potential_match = targetSum - num
# if difference already exists in the dictionary then we have our second number
        if potential_match in nums:
            return [num, potential_match]
        else:
# if difference doesn't exist in the dictionary, then we add it to the dictionary and assign a boolean as value to it            
            nums[num] = True
# if we don't find a match then we return and empty list
    return []