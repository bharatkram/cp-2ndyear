# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def primeFactors(n):
    temp = n
    lis = [1]
    while temp % 2 == 0:
        temp //= 2
        lis.append(2)

    for i in range(3, int(n**0.5)+1, 2):
        while temp % i == 0:
            temp //= i
            lis.append(i)

    if temp > 2:
        lis.append(temp)
    return lis


def isPowerfulNumber(n):
    factors = primeFactors(n)
    for factor in factors:
        if n % factor**2 != 0:
            return False
    return True


def nthpowerfulnumber(n):
    # Your code goes here
    num = 0
    while n != -1:
        num += 1
        if isPowerfulNumber(num):
            n -= 1
    return num
