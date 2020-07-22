# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).


def longestdigitrun(n):
    # Your code goes here
    n = abs(n)
    digit = 10
    count = 0
    tempCount, tempDigit = 0, 0
    while n != 0:
        dig = n % 10
        n //= 10
        if dig != tempDigit:
            if tempCount > count:
                count = tempCount
                digit = tempDigit
            elif tempCount == count:
                digit = tempDigit if tempDigit < digit else digit
            tempCount = 1
            tempDigit = dig
        else:
            tempCount += 1

    if tempCount > count:
        digit = tempDigit
    elif count == tempCount and tempDigit < digit:
        digit = tempDigit
    return digit
