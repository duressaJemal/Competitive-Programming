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
    arr = inpli()

    total = sum(arr)
    target = (2 * total)/n

    counted = Counter(arr)
    count = 0
    for ele in arr:
        if target - ele in counted:
            if target == 2 * ele:
                count += counted[target - ele] - 1
            else:
                count += counted[target - ele]

            counted[ele] -= 1

            if counted[ele] == 0:
                del counted[target - ele]
    print(count)
        
        

    
t = inpnum()
while t:
    main()
    t -= 1

