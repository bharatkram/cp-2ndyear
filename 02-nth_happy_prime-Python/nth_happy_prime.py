# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def ishappynumber(n):
    if n < 1:
        return False
    pastDict = {}
    while n != 1:
        sum = 0
        while n != 0:
            sqDig = (n % 10)**2
            n //= 10
            sum += sqDig
        n = sum
        try:
            pastDict[n] += 1
            return False
        except KeyError:
            pastDict[n] = 1
    return True


def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def fun_nth_happy_prime(n):
    present = 8
    while True:
        if n == 0:
            return present - 1
        if ishappynumber(present) and isprime(present):
            n -= 1
        present += 1
