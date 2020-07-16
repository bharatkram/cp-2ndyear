# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


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
