# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math


def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def isrighttriangle(x1, y1, x2, y2, x3, y3):
    # your code goes here
    first, second, third = sorted([distance(x1, y1, x2, y2), distance(
        x2, y2, x3, y3), distance(x3, y3, x1, y1)])
    return math.isclose(third**2, first**2 + second**2)
