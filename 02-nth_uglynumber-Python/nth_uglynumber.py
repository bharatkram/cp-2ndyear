# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def isUglyNumber(num):
    while num % 2 == 0:
        num //= 2
    for i in range(3, 6):
        while num % i == 0:
            num //= 2
    return True if num == 1 else False


def fun_nth_uglynumber(n):
    # your code goes here
    num = 0
    while n != -1:
        num += 1
        if isUglyNumber(num):
            n -= 1
    return num
