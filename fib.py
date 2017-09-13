#!/usr/bin/env python3
import sequences
import sys

def main(local_argv):
    n = int(local_argv[1])
    print(sequences.fibonacci(n)[-1])

if __name__ == "__main__":
    main(sys.argv)