# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.


def onlyEvenDigits(lis, pos):
    if pos >= len(lis):
        return lis
    lis[pos] = 0 if (lis[pos] % 2) != 0 else lis[pos]
    return onlyEvenDigits(lis, pos + 1)


def fun_recursion_onlyevendigits(l):
    # Your code goes here
    return onlyEvenDigits(l, 0)
