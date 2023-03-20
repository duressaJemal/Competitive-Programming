from collections import Counter, defaultdict
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
    n, m = inpnums()
    arr = []

    for index in range(m):
        a, b = inpnums()
        arr.append([a, b])

    arr.sort()

    mn = arr[0][1]

    for index in range(1, m):
    
        if mn >= (arr[index][0] - 1):
            mn = max(mn, arr[index][1])
        else:
            print("YES")
            return

    if mn < (n - 1) or arr[0][0] > 0:
        print("YES")
    else:
        print("NO")

    return

main()