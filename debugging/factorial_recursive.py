#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): non-negative integer whose factorial is to be computed

    Return:
    int: factorial of n (n!), which is the product of all integers from 1 to n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
