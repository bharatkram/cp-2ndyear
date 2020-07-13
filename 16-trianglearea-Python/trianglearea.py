# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def islegaltriangle(s1, s2, s3):
    return (s1 > 0 and s2 > 0 and s3 > 0) and (max(s1, s2, s3) < s1 + s2 + s3 - max(s1, s2, s3))


def trianglearea(s1, s2, s3):
    # your code goes here
    if not islegaltriangle(s1, s2, s3):
        return 0
    return (0.25) * ((s1 + s2 + s3) * (s1 + s2 - s3) * (s3 + s1 - s2) * (s2 + s3 - s1))**0.5
