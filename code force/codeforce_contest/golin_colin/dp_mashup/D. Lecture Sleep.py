# Link: https://codeforces.com/gym/302977/problem/D
#Q: D. Lecture Sleep

# DP(prefix)

# Time: O(N)
# Space: O(N)

n , k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

unaffected_prefix = [0] * (n)
unaffected_prefix[0] = a[0] * t[0]
for i in range(1, n):
    unaffected_prefix[i] = a[i] * t[i] + unaffected_prefix[i - 1]

unaffected_suffix = [0] * (n)
total = 0

for i in range(n-1, -1, -1):
    total += a[i] * t[i]
    unaffected_suffix[i] = total

affected_prefix = [0] * (n)
total = 0
for i in range(n):
    total += a[i]
    affected_prefix[i] = total

answer = 0
i = 0
while i < n - k + 1:
# for i in range(n - k + 1): # how is this not working
    curr = 0
    if i > 0: curr += unaffected_prefix[i - 1]
    if (i + k) < n: curr += unaffected_suffix[i + k]
    affected_range = affected_prefix[i + k - 1]
    if i > 0: affected_range -= affected_prefix[i - 1]
    curr += affected_range
    answer = max(answer, curr)
    i += 1

print(answer)
    
