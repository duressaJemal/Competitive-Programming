# Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A
# Q:  Merging Arrays
# Two pointers
# Time: O(N + M)
# Space: O(N + M)

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = [0] * (len(arr1) + len(arr2))
i, j = 0, 0

while i < len(arr1) or j < len(arr2):
    if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
        res[i + j] = arr1[i]
        i += 1
    else:
        res[i + j] = arr2[j]
        j += 1

for num in res:
    print(num)