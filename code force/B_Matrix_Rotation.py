# Link: https://codeforces.com/problemset/problem/1772/B
#Q: B. Matrix Rotation

# Time: O(1)
# Space: O(1)

t = int(input())

def beautifull(grid):
    valid_row = grid[0][0] < grid[0][1] and grid[1][0] < grid[1][1]
    valid_column = grid[0][0] < grid[1][0] and grid[0][1] < grid[1][1]
    return  valid_row and valid_column

def rotate(grid):

    temp = grid[0][0]
    grid[0][1], temp = temp, grid[0][1]
    grid[1][1], temp = temp, grid[1][1]
    grid[1][0], temp = temp, grid[1][0]
    grid[0][0], temp = temp, grid[0][0]
    
for i in range(t):

    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))

    grid = [row1, row2]

    is_beautifull = False
    for i in range(4):
        if is_beautifull:
            break

        is_beautifull = is_beautifull or beautifull(grid)
        rotate(grid)

    print("YES" if is_beautifull else "NO")


# Alternative

# Time: O(1)
# Space: O(1)

t = int(input())

for _ in range(t):
    
    arr = []
    arr += list(map(int, input().split()))
    arr += list(map(int, input().split()))

    mn = [0, float("inf")]
    mx = [0, float("-inf")]

    for index, value in enumerate(arr):
        if value > mx[1]:
            mx = [index, value]
        if value < mn[1]:
            mn = [index, value]
    
    print("YES" if mx[0] + mn[0] == 3 else "NO")

     