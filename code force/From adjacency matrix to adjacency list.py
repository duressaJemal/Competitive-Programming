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

    for _ in range(n):
        res = []
        row = inpli()
        for index in range(n):
            if row[index] == 1:
                res.append(index + 1)
        
        res.sort()
        print(len(res), *res)
    

main()