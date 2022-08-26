# Link: https://codeforces.com/gym/395575/problem/C

# BFS

# Time: O()
# Space: O()

import collections


n, m = map(int, input().split())
queue = collections.deque([n])
level = 1
is_found = False
visited = {n}

while queue:

    for _ in range(len(queue)):
        parent = queue.popleft()

        if parent >= m:
            red = parent
        else:
            red = parent * 2

        blue = parent - 1
        
        if red == m or blue == m:
            is_found = True
            break

        if red > 0 and red not in visited:
            queue.append(red)
            visited.add(red)
        if blue > 0 and blue not in visited:
            queue.append(blue)
            visited.add(blue)

    if is_found:
        break

    level += 1

print(level)
