# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.


def isAutomorphic(num):
    squaredNum = num**2
    while num != 0:
        if num % 10 != squaredNum % 10:
            return False
        num //= 10
        squaredNum //= 10

    return True


def nthautomorphicnumbers(n):
    # Your code goes here
    if n <= 14:
        num = -1
        while n != 0:
            num += 1
            if isAutomorphic(num):
                n -= 1
        return num
    else:
        endWithFive = 2890625
        endWithSix = 7109376
        fiveDigits = 10**7
        sixDigits = 10**7
        while n > 14:
            flag5, flag6 = True, True
            while flag5:
                for digit in range(9, -1, -1):
                    newNum = endWithFive + digit * fiveDigits
                    if newNum**2 % (fiveDigits*10) == newNum:
                        if newNum == endWithFive:
                            fiveDigits *= 10
                            break
                        else:
                            flag5 = False
                            endWithFive = newNum
                            fiveDigits *= 10
                            break
            while flag6:
                for digit in range(9, -1, -1):
                    newNum = endWithSix + digit * sixDigits
                    if newNum**2 % (sixDigits*10) == newNum:
                        if newNum == endWithSix:
                            sixDigits *= 10
                            break
                        else:
                            flag6 = False
                            endWithSix = newNum
                            sixDigits *= 10
                            break
            n -= 2
        if n % 2 == 0:
            return min(endWithFive, endWithSix)
        else:
            return max(endWithFive, endWithSix)
