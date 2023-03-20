from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

def inp():
    return int(stdin.readline())
def inlt():
    return list(map(int, stdin.readline().strip().split()))
def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])
def inm():
    return map(int, stdin.readline().strip().split())

def main():
    n = inp()
    arr = inlt()

    # prefix
    prefix = [0] * n
    prefix[0] = arr[0]

    for index in range(1, n):
        prefix[index] = prefix[index - 1] + arr[index]
    
    # init
    total = prefix[11] if n >= 12 else prefix[-1]
    
    if n > 12:
        for index in range(12, n):
            if not (index % 6):
                curr = prefix[min(n - 1, index + 11)] - prefix[index] + arr[index]
                total = min(total, curr)
                
    print(total)
    return

t = inp()
while t:
    main()
    t -= 1
