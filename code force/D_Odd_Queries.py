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
    
    n, q = inpnums()
    arr = inpli()
    prefix = [0] * (n + 1)

    for index in range(1, n + 1):
        prefix[index] = prefix[index - 1] + arr[index - 1]

    total = sum(arr)

    for _ in range(q):

        l, r, k = inpnums()

        segment = prefix[r] - prefix[l - 1]
        new = k * (r - l + 1)

        res = total - segment + new

        if res % 2:
            print("YES")
        else:
            print("NO")
        
    return
    


t = inpnum()
while t:
    main()
    t -= 1

