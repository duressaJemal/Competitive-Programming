from collections import defaultdict


n, k = map(int, input().split())
arr = list(map(int, input().split()))

counter = defaultdict(int)
res = 0

left = 0

for right in range(n):

    # add
    counter[arr[right]] += 1

    # validate
    while len(counter) > k:

        # remove
        counter[arr[left]] -= 1
        if not counter[arr[left]]:
            counter.pop(arr[left])
        left += 1
    
    res += (right - left + 1)

print(res)
