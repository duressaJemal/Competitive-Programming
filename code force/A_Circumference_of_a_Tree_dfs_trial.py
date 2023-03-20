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
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v = inpnums()
        graph[u].append(v)
        graph[v].append(u)

    if len(graph) == 0:
        print(0)
        return
    
    start = list(graph.keys())[0]
    
    deepest = (0, start)

    def dfs(node, far):
        nonlocal deepest

        visited[node] = True
        deepest = max(deepest, (far, node))
            
        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei, far + 1)
    
    visited = defaultdict(int)
    dfs(start, 0)
    visited = [False for _ in range(n + 1)]
    dfs(deepest[1], 0)
    print(deepest[0]*3)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

