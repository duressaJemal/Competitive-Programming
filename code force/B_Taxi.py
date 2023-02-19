from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

counter = Counter(arr)
output = 0

four = counter[4]
three = counter[3]

# +3 accounting for odd len of two and ones
two_one = ((counter[2] * 2 + max(0, counter[1] - counter[3])) + 3) // 4

output = four + three + two_one
print(output)




