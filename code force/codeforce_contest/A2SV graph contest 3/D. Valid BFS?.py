# Link: https://codeforces.com/gym/395575/problem/D
# q: D. Valid BFS?

import collections

n = int(input())
edges = collections.defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

arr = list(map(int, input().split()))

queue = collections.deque([(1, 0)]) # node, parent

node_level = {1 : 1}
level = 1

while queue:
    level += 1
    for _ in range(len(queue)):
        parent = queue.popleft()
        for child in edges[parent[0]]:
            if child != parent[1]:
                queue.append((child, parent[0]))
                node_level[child] = level

current_level = 1
is_valid = True


for value in arr:

    if current_level > node_level[value]:
        is_valid = False
        break
    current_level = node_level[value]

print("YES" if is_valid else "NO")




        





