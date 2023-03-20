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
    arr= inpli()

    count = [0]

    def merge(l, r):

        if l == r:
            return [arr[l]]
        
        mid = l + (r - l) // 2

        left = merge(l, mid)
        right = merge(mid + 1, r)

        if left and right:
            if left[-1] < right[0]:
                return left + right
            elif right[-1] < left[0]:
                count[0] += 1
                return right + left
            else:
                return False
        else:
            return False

    value = merge(0, len(arr) - 1)
    
    if value:
        print(count[0])
    else:
        print(-1)
        

t = inpnum()
while t:
    main()
    t -= 1

