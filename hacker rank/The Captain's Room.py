# Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=false
#Q: The Captain's Room

# Time: O(N)
# Space: O(N)

from collections import Counter
n = int(input())

counter = Counter(list(map(int, input().split())))
for key in counter:
    if counter[key] != n:
        print(key)

