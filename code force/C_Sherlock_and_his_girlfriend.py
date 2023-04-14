from collections import Counter
from functools import lru_cache
import math
import threading
from sys import stdin,stdout,setrecursionlimit

def inp():
    return stdin.readline()

def inpnum():
    return int(stdin.readline())

def inpli():
    return list(map(int, stdin.readline().strip().split()))

def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])

def inpnums():
    return map(int, stdin.readline().strip().split())

def main():
    n = inpnum()
    is_prime = [True] * (n + 2)
    is_prime[0] = False
    is_prime[1] = False

    def SieveOfEratosthenes(n):
        p = 2
        while(p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

    SieveOfEratosthenes(n + 1)
    output = []
    for index in range(2, n + 2):
        if is_prime[index]:
            output.append(1)
        else:
            output.append(2)
    
    counter = Counter(output)
    print(len(counter))
    print(*output)
    return

main()

