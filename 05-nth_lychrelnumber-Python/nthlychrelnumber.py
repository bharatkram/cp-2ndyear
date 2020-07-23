# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def isPalindrome(n):
    rev = revNumber(n)
    return rev == n


def revNumber(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev


def lychrelNumber(n):
    for i in range(25):
        if isPalindrome(n):
            return False
        n += revNumber(n)
    return True


def nthlychrelnumbers(n):
    # your code goes here
    num = 0
    while n != 0:
        num += 1
        if lychrelNumber(num):
            n -= 1
    return num
