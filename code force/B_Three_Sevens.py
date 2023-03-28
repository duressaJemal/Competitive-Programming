from collections import defaultdict
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
    
    m = inpnum()
    total = []
    counter = defaultdict(int)

    for _ in range(m):

        n = inpnum()
        arr = inpli()

        for i in range(n):
            counter[arr[i]] += 1

        total.append(arr)
    
    res = []
    for arr in total:
        added = False
        for val in arr:
            if counter[val] == 1:
                if not added:
                    added = True
                    res.append(val)
            counter[val] -= 1
        if not added:
            print(-1)
            return

    print(*res)
    return


t = inpnum()
while t:
    main()
    t -= 1

 