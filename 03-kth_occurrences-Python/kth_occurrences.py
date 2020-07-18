# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    # your code goes here
    charDict = {}
    for char in s:
        try:
            charDict[char] += 1
        except KeyError:
            charDict[char] = 1
    lis = sorted(charDict.values())
    n = lis[n - 1]
    for key in charDict.keys():
        if charDict[key] == n:
            return key
    return -1
