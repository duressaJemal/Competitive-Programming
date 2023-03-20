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
    
    l = inpnum()
    arr = []

    for _ in range(l):
        curr = list(input().split())
        arr.append(curr)

    mx = 2**32

    stack = []
    total = 1

    output = 0

    for val in arr:
        
        if len(val) == 2:
            if stack:
                stack.append(min(mx, stack[-1] * int(val[1])))
            else:
                stack.append(min(mx, int(val[1])))
        else:

            if val[0] == "add":
                if stack:
                    output += (1 * stack[-1])
                else:
                    output += 1

            else:
                stack.pop()
    
    if output >= mx:
        print("OVERFLOW!!!")
    else:
        print(output)




main()

