# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True if num >= 2 else False


def isLeftTruncablePrime(num):
    if not isPrime(num):
        return False
    pwr = 1
    prev = 0
    while num // 10**pwr > 0:
        part = num % 10**pwr
        if part == prev or not isPrime(part):
            return False
        pwr += 1
        prev = part
    return True


def fun_nth_lefttruncatableprime(n):
    # your code goes here
    num = 1
    while n != -1:
        num += 1
        if isLeftTruncablePrime(num):
            n -= 1
    return num
