from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

def inp(): return stdin.readline()
def inpnum(): return int(stdin.readline())
def inpli(): return list(map(int, stdin.readline().strip().split()))
def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])
def inpnums():return map(int, stdin.readline().strip().split())
def main():

    n = inpnums()
    arr = inpli()

    for i in range(n):
        for j in range(n):
            ...
            

main()