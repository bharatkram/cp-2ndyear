# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sumOfSquaresOfDigits(n):
    total = 0
    while n != 0:
        total += (n % 10)**2
        n //= 10
    return total


def isHappyNumber(n):
    while n not in [1, 4]:
        n = sumOfSquaresOfDigits(n)
    if n == 4:
        return False
    return True


def ishappyprimenumber(n):
    # Your code goes here
    if isPrime(n) and isHappyNumber(n):
        return True
    return False
