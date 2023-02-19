t = int(input())

for _ in range(t):

    grid = []

    for row in range(8):
        row = list(input())
        grid.append(row)

    is_found = False

    for row in range(1, 7):
        for col in range(1, 7):
            if grid[row][col] == "#":
                if grid[row + 1][col + 1] == "#" and grid[row - 1][col - 1] == "#" and grid[row - 1][col + 1] == "#" and grid[row + 1][col - 1] == "#":
                    is_found = True
                    break
        if is_found:
            break
    
    print(row + 1, col + 1)
    
    
 

