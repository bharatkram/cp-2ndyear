# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def circularNumbers(n):
    temp = n
    countOfDigits = 0
    while temp != 0:
        dig = temp % 10
        if dig == 0:
            return [], True
        countOfDigits += 1
        temp //= 10

    lis = [n]
    for i in range(1, countOfDigits):
        n = (n % 10**(countOfDigits-1))*10 + n//10**(countOfDigits-1)
        lis.append(n)
    return lis, False


def isCircularPrime(n):
    lis, zeroFound = circularNumbers(n)
    if zeroFound:
        return False
    for num in lis:
        if not isPrime(num):
            return False
    return True


def nthcircularprime(n):
    # Your code goes here
    num = 1
    while n != 0:
        num += 1
        if isCircularPrime(num):
            n -= 1
    return num
