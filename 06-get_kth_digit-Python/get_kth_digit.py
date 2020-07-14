# Write the function getKthDigit(n, k) that takes
# a possibly-negative int n and a non-negative int k,
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0


def fun_get_kth_digit(digit, k):
    # your code goes here.
    if k % 10**digit == 0:
        return 0
    return (k // 10**digit) % 10
