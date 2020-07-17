# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isPalindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def fun_nth_palindromic_prime(n):
    if n == 0:
        return 2
    current = 3
    while True:
        if n == 0:
            return current - 1
        if isPrime(current) and isPalindrome(str(current)):
            n -= 1
        current += 1
