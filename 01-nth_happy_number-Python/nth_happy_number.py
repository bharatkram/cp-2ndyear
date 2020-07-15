# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


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


def fun_nth_happy_number(n):
    # your code goes here
    present = 1
    while True:
        if ishappynumber(present):
            n -= 1
        if n == 0:
            return present
        present += 1
