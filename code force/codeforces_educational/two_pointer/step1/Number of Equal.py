# Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C
# Q: Number of Equal

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0

start, end = 0, 0
previous = 0

for i in range(n):
    if arr1[i] == previous: 
        count += end - start
        continue
    else:
        start = end
        while True:
            if end == len(arr2) or arr1[i] < arr2[end]:
                # calculate
                count += end - start
                break
            elif arr1[i] > arr2[end]:
                end += 1
                start = end
            elif arr1[i] == arr2[end]:
                end += 1
        previous = arr1[i]

print(count)


