# Write the function alternatingSum(L) that takes a possibly-empty list of numbers,
# and returns the alternating sum of the list, where every other value is subtracted
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def lisSum(l, i, s):
    if i == len(l):
        return s
    elif i % 2 == 0:
        s += l[i]
    else:
        s -= l[i]
    return lisSum(l, i+1, s)


def fun_recursions_alternatingsum(l):
    return lisSum(l, 0, 0)
