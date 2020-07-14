# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.
import math


def coeff(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def fun_pascaltrianglevalue(row, col):
    # your code goes here
    if row < 0 or col < 0 or row + 1 < col:
        return 0
        if row == 1:
            return 1
    return coeff(row - 1, col - 1) + coeff(row - 1, col)
