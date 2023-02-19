
# DFS

# Time: O(N^2)
# Space: O(N^2)

# import collections
# import sys
# sys.setrecursionlimit(10**7)

# n = int(input())
# ax, ay = map(int, input().split())
# bx, by = map(int, input().split())
# cx, cy =  map(int, input().split())
# dirc = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
# visited = set()

# def dfs(r, c):
#     if r < 1 or r > n or c < 1 or c > n: return False
#     if (r, c) in visited: return False
#     visited.add((r, c))
#     if r == ax or c == ay: return False # case for 4 directional match
#     if abs(r - ax) == abs(c - ay): return False # case for diagonal
    
#     if (r, c) == (cx, cy): return True
    
#     value = False
#     for x, y in dirc:
#         nr = r + x
#         nc = c + y

#         if value: return True
#         value = value or dfs(nr, nc)

#     return value
    
# print ("YES" if dfs(bx, by) else "NO")

# BFS

# Time: O(N^2)
# Space: O(N^2)

# import collections


# n = int(input())
# ax, ay = map(int, input().split())
# bx, by = map(int, input().split())
# cx, cy =  map(int, input().split())
# dirc = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
# visited = set()

# queue = collections.deque([(bx, by)])

# is_found = False
# while queue:
#     r, c = queue.popleft()

#     for x, y in dirc:
#         nr = r + x
#         nc = c + y
        
#         if (nr, nc) in visited: continue
#         visited.add((nr, nc))
#         if nr < 1 or nr > n or nc < 1 or nc > n: continue
#         if nr == ax or nc == ay: continue # case for 4 directional check
#         if abs(nr - ax) == abs(nc - ay): continue # case for diagonal check

#         if (nr, nc) == (cx, cy): 
#             is_found = True
#             break

#         queue.append((nr,nc))

#     if is_found:
#         break

    

# print("YES" if is_found else "NO")
        

n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy =  map(int, input().split())

def determine_quadrant(x, y):
    value = ""
    if x < ax: # upper half
        if y < ay:
            value = "UL"
        else:
            value = "UR"

    else: # lower half
        if y < ay:
            value = "BL"
        else:
            value = "BR"
    return value

if determine_quadrant(bx, by) == determine_quadrant(cx, cy):
    print("YES")
else:
    print("NO")
