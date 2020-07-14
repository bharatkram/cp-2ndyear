# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.


def fun_pascaltrianglevalue(row, col):
    # your code goes here
    if row < 0 or col < 0 or row + 1 < col:
        return 0
    row = tuple(str(11**(row - 1)))
    return int(row[col])
