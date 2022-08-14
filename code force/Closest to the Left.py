n , k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for i in range(k):

    left = -1 # arr[i] <= target
    right = n # arr[i] > target

    while right > left + 1:

        mid = (left + right) // 2
        if arr[mid] <= queries[i]:
            left = mid
        else:
            right = mid
    
    print(left + 1)


