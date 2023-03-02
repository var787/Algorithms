# single line method O(nlog(n)) time | O(n) space
def sortedSquaredArray(array):
    return sorted([x**2 for x in array])
