# Write the function smallestDifference(a) that takes a list of integers and returns
# the smallest absolute difference between any two
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
    # Your code goes here
    a = sorted(a)
    smallest = -1
    pastEle = a[0]
    for i in range(1, len(a)):
        diff = abs(pastEle - a[i])
        smallest = diff if ((diff < smallest) or (
            smallest == -1)) else smallest
        pastEle = a[i]
    return smallest
