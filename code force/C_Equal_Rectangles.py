from collections import Counter
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
    counter = Counter(inpli())

    temp = []
    is_valid = True

    for key in counter:

        if counter[key] % 2:
            is_valid = False
            break
        else:
            temp.extend([key] * (counter[key] // 2))
      
    if not is_valid:
        print("NO")
        return

    temp.sort()

    cur = temp[0] * temp[-1]

    left = 0
    right = len(temp) - 1

    while left < right:
        if temp[left] * temp[right] != cur:
            is_valid = False
            break
            
        left += 1
        right -= 1
    
    if is_valid:
        print("YES")
    else:
        print("NO")
    
    return 

t = inpnum()
while t:
    main()
    t -= 1



    




