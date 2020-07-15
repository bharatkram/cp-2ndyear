# Write the function fun_threelines_area(d1, d2, d3)
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.
import math


def fun_threelines_area(a, b, c):
    return 0.25 * ((s1 + s2 + s3) * (s1 + s2 - s3) * (s2 + s3 - s1) * (s3 + s1 - s2))**0.5
