# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.


def isAutomorphic(num):
    numOfDigits = 1
    temp = num//10
    while temp != 0:
        numOfDigits += 1
        temp //= 10

    squaredNum = num**2

    return True if squaredNum % 10**numOfDigits else False


def nthautomorphicnumbers(n):
    # Your code goes here
    num = -1
    while n != 0:
        num += 1
        if isAutomorphic(num):
            n -= 1
    return num
