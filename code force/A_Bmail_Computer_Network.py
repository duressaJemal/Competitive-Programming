from collections import defaultdict, deque
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
    parent = inpli()

    ans = [n]

    while ans[-1] != 1:
        ans.append(parent[ans[-1] - 2])
    
    print(*reversed(ans))

    # Alternative

    # n = inpnum()
    # arr = inpnums()

    # graph = {1: - 1}
    # for index, parent in enumerate(arr):
    #     node = index + 2
    #     graph[node] = parent
    
    # output = []
    # current = n

    # while current != -1:
    #     output.append(current)
    #     current = graph[current]
        
    
    # print(*output[::-1])



main()
