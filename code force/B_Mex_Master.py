from functools import lru_cache
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
    arr = inpli()

    arr.sort()

    zeros = []
    non_zeros = []

    for val in arr:
        if val:
            non_zeros.append(val)
        else:
            zeros.append(val)
    
    l_zeros = len(zeros)
    l_non_zeros = len(non_zeros)

    if not zeros or l_zeros <= l_non_zeros + 1:
        print(0)
        return 
    else:
        if not non_zeros or non_zeros[-1] != 1:
            print(1)
        else:
            print(2)
        
        return

t = inpnum()
while t:
    main()
    t -= 1

