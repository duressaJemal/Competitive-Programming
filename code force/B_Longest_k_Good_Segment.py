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
    n, k = inpnums()
    arr = inpli()

    res = (0, (0, 0))

    dic = defaultdict(int)

    left = 0

    for right in range(n):

        # add
        dic[arr[right]] += 1

        while len(dic) > k: # invalid
            # remove
            dic[arr[left]] -= 1
            if not dic[arr[left]]:
                dic.pop(arr[left])
            left += 1
        
        res = max(res, (right - left + 1, (left, right)))
    
    
    print(res[1][0] + 1, res[1][1] + 1)
        




main()