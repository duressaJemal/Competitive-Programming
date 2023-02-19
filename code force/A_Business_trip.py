k = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
current = 0

for index in range(len(arr) - 1, -1, -1):
    if current < k:
        current += arr[index]
        count += 1
    else:
        break

print(count if current >= k else -1)