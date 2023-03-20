from bisect import bisect_left
from functools import lru_cache
from itertools import accumulate
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
    
    n, q = inpnums()
    wor = inpli()
    defe = inpli()

    prefix = list(accumulate(wor))
    output = []
    current_index = 0

    for value in defe:

        current_index = bisect_left(prefix[current_index:], value + prefix[current_index])
        if current_index == len(wor) - 1:
            current_index = 0

        
        standing = len(wor) - current_index
        output.append(standing)
    








main()
# t = inp()
# while t:
#     main()
#     t -= 1

