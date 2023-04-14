from collections import defaultdict
from functools import lru_cache
import threading
from sys import stdin, stdout, setrecursionlimit


def inp(): return stdin.readline()
def inpnum(): return int(stdin.readline())
def inpli(): return list(map(int, stdin.readline().strip().split()))


def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])


def inpnums(): return map(int, stdin.readline().strip().split())


def main():
    n = inpnum()
    graph = defaultdict(list)

    for index in range(n):
        row = inpli()
        for i in range(1, row[0] + 1):
            graph[row[i]].append(index + 1)


    def bipartite(node, color):
        visited[node] = color
        for child in graph[node]:
            if child in visited:
                if visited[child] == color:
                    return False
            else:
                if not bipartite(child, 1 - color):
                    return False
        return True
    
    is_valid = True
    for node in range(1, n + 1):
        visited = {}
        if not bipartite(node, 1):
            is_valid = False
            break

    if is_valid:
        print(":)")
    else:
        print(":(")


main()
