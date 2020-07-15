# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.


def powersOf3ToN(lis, pos, n):
    if 3**pos > n:
        return lis
    lis.append(3**pos)
    return powersOf3ToN(lis, pos + 1, n)


def recursion_powersof3ton(n):
    # Your code goes here
    return None if n < 1 else powersOf3ToN([], 0, n)
