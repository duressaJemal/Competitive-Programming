# Link: https://codeforces.com/gym/302977/problem/A
#Q: A. Filling Shapes

# DP

# Time: O(N)
# Space: O(N)

n = int(input())
arr = [0] * (n + 1)

arr[0] = 1

for i in range(2, n + 1):
    arr[i] = 2 * arr[i - 2]

print(arr[n])
