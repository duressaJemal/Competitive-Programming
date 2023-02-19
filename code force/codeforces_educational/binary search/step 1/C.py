n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for i in range(k):

    left = -1 # arr[mid] <
    right = n # arr[mid] >=

    while right > left + 1:
        mid = (left + right) // 2

        if arr[mid] < queries[i]:
            left = mid
        else:
            right = mid

    print(right + 1)



