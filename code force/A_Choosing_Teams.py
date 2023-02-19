n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_participation = 5 - k

count = 0
for num in arr:
    if num <= min_participation:
        count += 1
    
print(count // 3)