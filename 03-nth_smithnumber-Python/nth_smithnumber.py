# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
from math import sqrt


def sumOfDigits(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total


def primeFactors(n):
    lis = []
    for i in range(2, int(n//2)+1):
        while n % i == 0:
            n //= i
            lis.append(i)
        if n == 1:
            break
    return (lis, False if n > 2 else True)


def isSmithNumber(n):
    lisOfFactors, flag = primeFactors(n)
    return flag and sumOfDigits(n) == sumOfDigits(sum(lisOfFactors))


def fun_nth_smithnumber(n):
    # your code goes here
    num = 3
    while n != -1:
        num += 1
        if isSmithNumber(num):
            n -= 1
    return num
