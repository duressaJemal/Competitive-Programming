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
    
    n, h = inpnums()
    time = inpli()

    def is_good(k):
        
        total = 0
        index = 0

        while index < n:
            
            dis = k
            if index + 1 < n:
                dis = min(dis, time[index + 1] - time[index])
            
            total += dis
            index += 1
        
        return total >= h
    
    left = 0 # invalid
    right = h

    while right > left + 1:

        mid = left + (right - left) // 2

        if is_good(mid):
            right = mid
        else:
            left = mid

        
    print(right)
    return


t = inpnum()
while t:
    main()
    t -= 1

