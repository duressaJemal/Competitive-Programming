# Link: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=false
#Q: Word Order

# Time: O(N)
# Space: O(N)

from collections import Counter

n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = input()

counter = Counter(arr)

print(len(counter))
for key in counter:
    print(counter[key], end = " ")

