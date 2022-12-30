# Link: https://codeforces.com/gym/418150/problem/E
#Q: Traffic Light

# Time: O(N)
# Space: O(N)

t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)

    given = input()
    given += given

    green_index = 0
    steps = 0

    if c != "g":
        for color_index in range(n):
            if given[color_index] == c:
                # find the green index
                for i in range(green_index, 2 * n):
                    if given[i] == "g":
                        if i >= color_index:
                            steps = max(steps, i - color_index)
                            green_index = i
                            break

    print(steps)





        
        
    
