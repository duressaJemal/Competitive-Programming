# Link: https://codeforces.com/contest/1676/problem/D
#Q: D. X-Sum

# Time: O(M*N)
# Space: O(M + N)

from collections import defaultdict

t = int(input())
for _ in range(t):

    n, m = map(int, input().split())
    grid = []
    right_digonal = defaultdict(int)
    left_digonal = defaultdict(int)
    output = 0
    
    # intput
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    # build digonal mapping
    for row in range(n):
        for col in range(m):
            # right digonal
            right_digonal[row - col] += grid[row][col]
            # left digonal
            left_digonal[row + col] += grid[row][col]

    # iterate over each value
    for row in range(n):
        for col in range(m):
            output = max(output, right_digonal[row - col] + left_digonal[row + col] - grid[row][col])

    print(output)