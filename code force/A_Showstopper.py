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
    a = inpli()
    b = inpli()

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
    
    mx_a = max(a)
    mx_b = max(b)

    if mx_a != a[-1] or mx_b != b[-1]:
        print("No")
    else:
        print("Yes")

    return

t = inpnum()
while t:
    main()
    t -= 1

 