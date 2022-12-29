# Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=false
#Q: DefaultDict Tutorial

# Time: O(N)
# Space: O(N)

from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)

for i in range(1, n + 1):
    a[input()].append(i)

for i in range(m):
    entry = input()
    if a[entry]:
        print(*a[entry])
    else:
        print(-1)
