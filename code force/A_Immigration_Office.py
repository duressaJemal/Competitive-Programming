from bisect import bisect_left

n = int(input())
arr = list(input().split())

q = int(input())
for _ in range(q):
    print(bisect_left(arr, input()))
