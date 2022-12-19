# Link: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=false
#Q: No Idea!

# Time: O(N)
# Space: O(N)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0
for i in range(n):
    if arr[i] in a:
        happiness += 1
    if arr[i] in b:
        happiness -= 1

print(happiness)
