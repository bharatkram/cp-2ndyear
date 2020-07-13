# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.


def islegaltriangle(s1, s2, s3):
    return (s1 > 0 and s2 > 0 and s3 > 0) and (max(s1, s2, s3) < s1 + s2 + s3 - max(s1, s2, s3))


def trianglearea(s1, s2, s3):
    if not islegaltriangle(s1, s2, s3):
        return 0
    return (0.25) * ((s1 + s2 + s3) * (s1 + s2 - s3) * (s3 + s1 - s2) * (s2 + s3 - s1))**0.5


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)


def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
    # your code goes here
    return trianglearea(distance(x1, y1, x2, y2), distance(x2, y2, x3, y3), distance(x3, y3, x1, y1))
