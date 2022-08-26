# Link: https://codeforces.com/gym/395575/problem/B

# BFS

# Time: O(N)
# Space: O(N)

import collections

n = int(input())
edges = {"polycarp": []}
for _ in range(n):
    u, r, v = input().split()
    u = u.lower()
    v = v.lower()
    edges[v].append(u)
    edges[u] = []

queue = collections.deque(["polycarp"])
level = 0

while queue:
    for _ in range(len(queue)):
        parent = queue.popleft()
        for child in edges[parent]:
            queue.append(child)
    level += 1

print(level)
