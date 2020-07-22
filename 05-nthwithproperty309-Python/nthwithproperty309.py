# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.


def hasProperty(num):
    arr = [0] * 10
    while num != 0:
        arr[num % 10] += 1
        num //= 10
    return 0 not in arr


def nthwithproperty309(n):
    # Your code goes here
    num = 308
    while n != -1:
        num += 1
        if hasProperty(num**5):
            n -= 1
    return num
