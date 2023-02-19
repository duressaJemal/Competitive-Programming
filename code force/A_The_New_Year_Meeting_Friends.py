points = list(map(int, input().split()))
points.sort()
print((points[1] - points[0]) + points[2] - points[1])