# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.


def onlyEvenDigits(ele, div):
    if ele % div == 0:
        return ele
    secPart = ele % div
    firPart = ele // div
    dig = secPart // (div/10)
    if dig % 2 == 0:
        return onlyEvenDigits(firPart*div+secPart, div*10)
    else:
        return onlyEvenDigits(firPart*(div/10)+secPart % (div/10), div)


def fun_recursion_onlyevendigits(l):
    # Your code goes here
    l = [onlyEvenDigits(ele, 10) for ele in l]
    return l
