def dfs(r, c):
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