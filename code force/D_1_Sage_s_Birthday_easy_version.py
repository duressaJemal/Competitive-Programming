n = int(input())
arr = list(map(int, input().split()))
arr.sort()

temp = []

left = 0
right = n - 1

while left <= right:
    temp.append(arr[right])
    if left != right:
        temp.append(arr[left])
    
    left += 1
    right -= 1


count = 0
for index in range(1, n - 1):
    if temp[index] < temp[index - 1] and temp[index] < temp[index + 1]:
        count += 1

if count:
    print(count)
    print(*temp)
else:
    print(count)
    print(*arr)
