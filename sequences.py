#!/usr/bin/env python3

def fibonacci(n):
    """Prints the first n fibonacci elements"""
    n0 = 0
    n1 = 1
    fib_list = []
    for i in range(n):
        fib_list.append(n1)
        (n0, n1) = (n1, n0+n1)
    return fib_list
    
print(fibonacci(1000)[-1])

