# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.
import math


def kaprekarNumber(num):
    squared = num**2
    pwr = 1
    while squared // 10**pwr != 0:
        fir = squared // 10**pwr
        sec = squared % 10**pwr
        if fir+sec == num:
            return True
    return False


def fun_nth_kaprekarnumber(n):
    # your code goes here
    if n == 0:
        return 1
    num = 8
    while n != -1:
        num += 1
        if kaprekarNumber(num):
            n -= 1
    return num
