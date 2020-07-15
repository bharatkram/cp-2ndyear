# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    # your code goes here
    lis = [0 * 10]
    while n != 0:
        lis[n % 10] += 1
        n //= 10
    return lis.index(max(lis))
