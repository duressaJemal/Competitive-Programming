# Run Time Error

n, m = map(int, input().split())
amount = list(map(int, input().split()))
visited = set()

edges = {}

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u in edges:
        edges[u].append(v)
    else:
        edges[u] = [v]
    
    if v in edges:
        edges[v].append(u)
    else:
        edges[v] = [u]


def dfs(node):
    minimum = amount[node]
    visited.add(node)

    if node in edges:
        for pair_node in edges[node]:
            if pair_node not in visited:
                minimum = min(minimum, dfs(pair_node))
    return minimum

answer = 0
for i in range(n):
    if i not in visited:
        answer += dfs(i)

print(answer)

