# Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B
# Q: Number of Smaller

# Two pointers
# Time: O(N + M)
# Space: O(M)

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = [0] * len(arr2)

i, j = 0, 0
while i < len(arr1) or j < len(arr2):
    if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
        i += 1
    else:
        res[j] = i
        j += 1

for num in res:
    print(num)

