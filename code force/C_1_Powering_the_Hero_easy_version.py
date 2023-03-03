from collections import Counter
from heapq import heapify, heappop, heappush



def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    result = 0

    nums = []
    heapify(nums)

    for val in arr:
        if val:
            heappush(nums, -val)
        else:
            if nums:
                result += (0 - heappop(nums))
    
    print(result)

t = int(input())
while t:
    solve()
    t -= 1