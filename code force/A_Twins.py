n = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = sum(arr)
middle_value = total / 2

current = 0
count = 0

for index in range(len(arr) - 1, - 1, - 1):
    current += arr[index]
    count += 1

    if current > middle_value:
        break
    
print(count)
