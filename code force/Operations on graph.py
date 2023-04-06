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
    n = inpnum()
    k = inpnum()

    graph = defaultdict(list)

    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)

    def vertex(u):
        return graph[u]
    
    for _ in range(k):
        
        cur = inpli()
        if len(cur) == 3:
            add_edge(cur[1], cur[2])
        else:
            print(*vertex(cur[1]))

main()
