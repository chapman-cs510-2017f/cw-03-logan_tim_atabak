#!/usr/bin/env python3

def fibonacci(n):
    """returns a list of the first n fibonacci values"""
    n0 = 0
    n1 = 1
    fib_list = []
    if type(n) != type(0) or n<=0:
        raise Exception("'%s' is not a positive int" % str(n))
    for i in range(n):
        fib_list.append(n1)
        (n0, n1) = (n1, n0+n1)
    return fib_list

def main():
    print(fibonacci(10))
    print(fibonacci('a'))
    
if __name__ == "__main__":
    main()