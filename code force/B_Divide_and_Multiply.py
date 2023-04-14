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
    
    count = 0

    for index in range(n):
        if arr[index] % 2 == 0:
            cur = arr[index]
            while cur % 2 == 0:
                count += 1
                cur = cur // 2
            arr[index] = cur
    
    arr.sort()
    largest = arr[-1]
    total = sum(arr) - largest

    res = total + (largest * (2 ** count))
    print(res)

t = inpnum()
while t:
    main()
    t -= 1

