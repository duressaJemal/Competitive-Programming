n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = int(input())

queries = []
for i in range(k):
    queries.append(list(map(int, input().split())))

for i in range(k):

    # greater than or equal to
    start = -1 # arr[mid] <
    end = n # arr[mid] >=

    while end > start + 1:

        mid = (start + end) // 2
        if arr[mid] < queries[i][0]:
            start = mid
        else:
            end = mid

    # less than or equal to

    left = -1 # arr[mid] <=
    right = n # arr[mid] >

    while right > left + 1:
        mid = (left + right) // 2
        if arr[mid] <= queries[i][1]:
            left = mid 
        else:
            right = mid
    
    if end > left:
        print(0)
    else:
        print(left - end + 1)


    
    
    
