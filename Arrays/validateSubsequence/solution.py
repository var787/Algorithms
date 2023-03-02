# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    # set counters for both
    arrayId = 0
    seqId = 0
    # while loop to traverse through the array for the length of the array
    while arrayId < len(array) and seqId < len(sequence):
        # increment sequence index if there is a match
        if array[arrayId] == sequence[seqId]:
            seqId += 1
        # keep increasing array index in every loop
        arrayId += 1
    # stop when index and length of array match, indicating end of the array
    return seqId == len(sequence)
