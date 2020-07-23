# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46


def isTidyNumber(n):
    prev = n % 10
    while n != 0:
        n //= 10
        if prev < n % 10:
            return False
        prev = n % 10
    return True


def fun_nth_tidynumber(n):
    # your code goes here
    num = 0
    while n != -1:
        num += 1
        if isTidyNumber(num):
            n -= 1
    return num
