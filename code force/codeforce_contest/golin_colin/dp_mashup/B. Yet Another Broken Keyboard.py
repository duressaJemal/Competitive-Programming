# Link: https://codeforces.com/gym/302977/problem/B
#Q: B. Yet Another Broken Keyboard

# DP

# Time: O(N)
# Space: O(N)

# Pull dp

n, k = map(int, input().split())
string = input()
typable = set(map(str, input().split()))

total = 0
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if string[i - 1] in typable:
        dp[i] = dp[i - 1] + 1
        total += dp[i]

print(total)

# Push dp

# n, k = map(int, input().split())
# string = input()
# typable = set(map(str, input().split()))

# total = 0
# dp = [0] * (n + 1)
# for i in range(n):
#     if string[i] in typable:
#         dp[i + 1] = dp[i] + 1
#         total += dp[i + 1]
#     else:
#         dp[i + 1] = 0
    
# print(total)
    




