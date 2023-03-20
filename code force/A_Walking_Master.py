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
    
    x1, y1, x2, y2 = inpnums()

    if y2 < y1:
        print(-1)
        return
    
    ver = y2 - y1
    x_new = x1 + ver

    if x_new < x2:
        print(-1)
        return
    
    hor = x_new - x2
    print(hor + ver)

t = inpnum()

while t:
    main()
    t -= 1

