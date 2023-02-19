n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

res = -1

if k == 0:
    if arr[0] > 1:
        res = 1 
else:
    for index in range(n):
        if index + 1 == k:
            if index + 1 < n:
                if arr[index] != arr[index + 1]:
                    res = arr[index]
                    break
            else:
                res = arr[index]
print(res)
