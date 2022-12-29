# Link: https://codeforces.com/problemset/problem/1730/A
#Q: Planets

# Time: O(N)
# Space: O(N)

from collections import Counter

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    planets = list(map(int, input().split()))

    counter = Counter(planets)
    output = 0

    for key in counter:
        if counter[key] <= c:
            output += counter[key]
        else:
            output += c
    
    print(output)

