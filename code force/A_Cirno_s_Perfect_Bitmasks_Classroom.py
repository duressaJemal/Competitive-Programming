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
    x = inpnum()
    bit_mask = 1

    if x == 1:
        print(3)
        return

    while (x & bit_mask) == 0:
        bit_mask = bit_mask << 1

    while not (bit_mask ^ x):
        bit_mask += 1

    print(bit_mask)

t = inpnum()
while t:
    main()
    t -= 1

