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

setrecursionlimit(2000000)
threading.stack_size(2**27)


def main():
    
    n = inpnum()

    # build graph
    graph = defaultdict(list)
    for node in range(1, n + 1):

        parent = inpnum()
        graph[parent].append(node)

    def dfs(node, parent, deepth):

        # base case
        if not graph[node]:
            return deepth

        curr  = 0
        for nei in graph[node]:
            if nei != parent:
                curr = max(curr, dfs(nei, node, deepth + 1))

        return curr

    # DFS
    roots = graph[-1]
    result = 0

    for root in roots:
        result = max(result, dfs(root, -1, 1))
    
    print(result)

    # BFS

    # def bfs(node):
    #     deepth = 0
    #     queue = deque([node, deepth])
    #     visited = set()

    #     while queue:
    #         n = len(queue)
    #         deepth += 1

    #         for _ in range(n):

    #             root = queue.popleft()
    #             visited.add(root)

    #             for nei in graph[root]:
    #                 if nei not in visited:
    #                     queue.append(nei)
    #     return deepth

    # result = 0
    # roots = graph[-1]

    # for root in roots:
    #     result = max(result, bfs(root))
    
    # print(result)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


