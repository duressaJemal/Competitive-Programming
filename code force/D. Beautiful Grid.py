import sys 

input = lambda:sys.stdin.readline().strip()

from math import ceil


t = int(input())

for _ in range(t):
    n = int(input())

    grid = []

    for _ in range(n):
        row = list(input())
        grid.append(row)
    
    total_operation = 0

    left, right = 0, n

    for i in range(n):
        for j in range(n):
            
            count = [0, 0]

            count[int(grid[i][j])] += 1
            count[int(grid[j][n - 1 - i])] += 1
            count[int(grid[n - 1 - i][n - 1 - j])] += 1
            count[int(grid[n - 1 - j][i])] += 1

            total_operation += min(count)
    
    print(total_operation // 4)



            



