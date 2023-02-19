n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

output = 0
for num in arr:
    if num < 0 and m > 0:
        output += num
        m -= 1
    else:
        break

print(0 - output)
