# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def isPrime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True


def isAdditivePrime(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return isPrime(total)


def fun_nth_additive_prime(n):
    current = 2
    while n != 0:
        if isPrime(current) and isAdditivePrime(n):
            n -= 1
        current += 1
    return current
