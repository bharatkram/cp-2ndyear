# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def isprime(ele):
    for i in range(2, int(ele**0.5) + 2):
        if ele % i == 0:
            return False
    return True


def fun_hasnoprimes(l):
    # your code goes here
    checked = []
    for row in l:
        for ele in row:
            if ele not in checked:
                if isprime(ele):
                    return False
                checked.append(ele)
    return True
