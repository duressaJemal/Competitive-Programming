# Link: https://codeforces.com/problemset/problem/90/B
#Q: B. African Crossword

# Time: O(M*N)
# Space: O(M + N)



from collections import Counter, defaultdict

row_len, col_len = map(int, input().split())

grid = []

for row in range(row_len):
    grid.append(list(input()))

row_map = {}
column_map = {}

# count row wise
for index, row in enumerate(grid):
    row_map[index] = Counter(row)

# count column wise
for c in range(col_len):
    temp = []
    for r in range(row_len):
        temp.append(grid[r][c])
    column_map[c] = Counter(temp)


for row in range(row_len):
    for col in range(col_len):

        current = grid[row][col]
        if current in column_map[col] and current in row_map[row]:
            if column_map[col][current] + row_map[row][current] > 2:
                grid[row][col] = ""

output = []
for row in grid:
    output += row

print("".join(output))

