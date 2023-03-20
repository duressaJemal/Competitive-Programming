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
    
    n, d = inpnums()
    arr = inpli()

    arr.sort()

    count = 0
    total = 0

    left = 0
    right = n - 1

    while left <= right:

        r = arr[right]
        total += r

        while left < right and total <= d:
            total += r
            left += 1
        
        if total > d:
            count += 1
        
        total = 0
        right -= 1
        
    print(count)

main()