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
    input()
    n, k = inpnums()
    friends = set(inpli())
    is_valid = False
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        u, v = inpnums()
        graph[u].append(v)
        graph[v].append(u)
    
    
    def bfs(node):

        nonlocal is_valid

        if node in friends:
            is_valid = False
            return
        
        from_source = float("inf")
        from_friend = float("inf")
    
        visited = set()
        visited.add(node)

        queue = deque([(node, 0)])

        while queue:
            
            n_len = len(queue)
            for _ in range(n_len):
                cur, length = queue.popleft()

                for child in graph[cur]:
                    if child not in visited:
                        if child in friends:
                            from_friend = min(from_friend, length)
                        elif child == 1:
                            from_source = min(from_source, length)
                        else:
                            visited.add(child)
                            queue.append((child, length + 1))

        if from_source < from_friend:
            is_valid = True
            return
        

    leaf_node = []
    for node in graph:
        if len(graph[node]) == 1:
            leaf_node.append(node)
    
    for node in leaf_node:
        bfs(node)
        if is_valid:
            print("YES")
            return
    
    print("NO")
    return

t = inpnum()
while t:
    main()
    t -= 1

