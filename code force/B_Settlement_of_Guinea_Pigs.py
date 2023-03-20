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

    result = 0
    total_count = 0
    ones_count = 0

    for value in arr:
        if value == 1:
            ones_count += 1
            total_count += 1
        else:
            if not (total_count - ones_count):
                result = max(result, ones_count)
            else:
                curr = ((total_count - ones_count) // 2 + 1) + ones_count
                result = max(result, curr)
            ones_count = 0

    if not (total_count - ones_count):
        result = max(result, ones_count)
    else:
        curr = ((total_count - ones_count) // 2 + 1) + ones_count
        result = max(result, curr)
    print(result)
        
t = inpnum()
while t:
    main()
    t -= 1

