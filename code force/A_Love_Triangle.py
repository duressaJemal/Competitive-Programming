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

    for index in range(n):
        cur = arr[index]

        B = arr[cur - 1]
        C = arr[B - 1]

        if C == (index + 1):
            print("YES")
            return

    print("NO")
    return
    
main()