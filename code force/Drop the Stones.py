t = int(input())

while t:
    n, m = map(int, input().split())
    grid = []
    
    for index in range(n):
        row = list(input())
        grid.append(row)
    
    def move_rock(grid, row, col):
        nr = row + 1
        while nr < n:
            if grid[nr][col] == "o":
                break
            else:
                grid[nr][col], grid[nr - 1][col] = grid[nr - 1][col], grid[nr][col]
            nr += 1


        
    for row in range(n - 1, -1, -1):
        for col in range(m):
            if grid[row][col] == "*":
                move_rock(grid, row, col)
    
    for row in range(n):
        print("".join(grid[row]))
    
    t -= 1
