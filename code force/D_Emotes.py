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

    n, m, k = inpnums()
    arr = inpli()

    arr.sort()

    b1 = arr[-1]
    b2 = arr[-2]
    total = 0

    total += (b1 * m)
    total -= (b1 - b2) * (m // (k + 1))
    
    print(total)
        


    

    
    
    

main()