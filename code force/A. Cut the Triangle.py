# Link: https://codeforces.com/problemset/problem/1767/A
#Q: A. Cut the Triangle

t = int(input())
for _ in range(t):

    input()
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    p3 = list(map(int, input().split()))

    x_points = [p1[0], p2[0], p3[0]]
    y_points = [p1[1], p2[1], p3[1]]

    arr = [p1, p2, p3]
    
    x_range = [min(x_points), max(x_points)]
    y_range = [min(y_points), max(y_points)]

    is_possible = False

    for point in arr:

        # horizontal line
        y = point[1]
        if y_points.count(y) == 1 and y_range[0] < y < y_range[1]:
            is_possible = True
            break

        # vertical line
        x = point[0]
        if x_points.count(x) == 1 and x_range[0] < x < x_range[1]:
            is_possible = True
            break
    
    print("YES" if is_possible else "NO")

# Alternative

t = int(input())
for _ in range(t):
    input()
    x_p = []
    y_p = []

    for _ in range(3):
        x, y = map(int, input().split())

        x_p.append(x)
        y_p.append(y)

    print("YES" if (len(set(x_p)) == 3 or len(set(y_p)) == 3) else "NO")



