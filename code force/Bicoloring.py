from collections import defaultdict
from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def inp(): return stdin.readline()
def inpnum(): return int(stdin.readline())
def inpli(): return list(map(int, stdin.readline().strip().split()))
def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])
def inpnums():return map(int, stdin.readline().strip().split())


def main():
    
    res = True
    while True:
        n = inpnum()
        if not n:
            break
        l = inpnum()

        # build graph
        graph = defaultdict(list)
        start = None
        for _ in range(l):
            u, v = inpnums()
            graph[u].append(v)
            graph[v].append(u)
 
        start = u
        def dfs(node, color):

            visited[node] = color
            for child in graph[node]:
                if child in visited:
                    if visited[child] == color:
                        return False
                else:
                    if not dfs(child, 1 - color):
                        return False
            
            return True
        
        visited = {}
        res  = dfs(start, 1)
        
        if res:
            print("BICOLOURABLE.")
        else:
            print("NOT BICOLOURABLE.")

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


