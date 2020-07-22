# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.


def isKaprekarNumber(num):
    squared = num**2
    pwr = 1
    while squared // 10**pwr > 0:
        fir = squared // 10**pwr
        sec = squared % 10**pwr
        if sec != 0 and fir + sec == num:
            return True
        pwr += 1
    return False


def fun_nearestkaprekarnumber(n):
    # your code goes here
    if isKaprekarNumber(n):
        return n
    negDirNum = n - 1
    posDirNum = n + 1
    flag = 0
    while True:
        if isKaprekarNumber(negDirNum):
            flag = -1
            break
        elif isKaprekarNumber(posDirNum):
            flag = 1
            break
        else:
            negDirNum -= 1
            posDirNum += 1
    return negDirNum if flag < 0 else posDirNum
