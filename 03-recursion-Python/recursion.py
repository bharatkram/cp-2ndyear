"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def rec_fib(pos, first, second):
    if pos == 0:
        return first
    return rec_fib(pos - 1, second, (first+second))


def get_fib(position):
    # your code goes here.
    return rec_fib(position, 0, 1)
