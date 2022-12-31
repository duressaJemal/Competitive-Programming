# Link: https://codeforces.com/gym/419351/problem/C
#Q: C_Amazing_Contests

# Time: O(N)
# Space: O(1)

n = int(input())
arr = list(map(int, input().split()))

mn, mx = arr[0], arr[0]

count = 0
for i in range(1, len(arr)):
    if arr[i] < mn:
        count += 1
        mn = arr[i]
    elif arr[i] > mx:
        count += 1
        mx = arr[i]

print(count)
