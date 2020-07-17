# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.


def checkfunction(str1, tup):
    str2, index = tup
    str2 = str2[index:] + str2[:index]
    return str1 == str2


def isrotated(str1, str2):
    # Your code goes here
    if len(str1) != len(str2):
        return False
    indexes = []
    char = str1[0]
    for index, letter in enumerate(str2):
        if letter == char:
            indexes.append(index)
    for index in indexes:
        check = str1[1]
        direction = 1 if check == str2[index +
                                       1 if index != len(str2) - 1 else 0] else -1 if check == str2[index - 1 if index != 0 else len(str2) - 1] else 0
        ret = checkfunction(str1, (str2, index) if direction ==
                            1 else (str2[::-1], len(str2)-(index+1))) if direction != 0 else False
        if ret == True:
            return True
    return False


def isrotation(x, y):
    # Your code goes here
    return isrotated(str(x), str(y))
