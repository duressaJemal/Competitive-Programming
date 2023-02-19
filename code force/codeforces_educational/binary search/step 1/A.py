n, k = map(int, input().split())
arr = list(map(int, input().split()))
targets = list(map(int, input().split()))

for i in range(k):
    left = -1 # a[mid] <= 
    right = n # a[mid] > 
    
    while right > left + 1:
        mid = (left + right) // 2
        if arr[mid] <= targets[i]:
            left = mid
        else:
            right = mid
    if arr[left] == targets[i]:
        print("YES")
    else:
        print("NO")
