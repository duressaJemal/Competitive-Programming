# Link: https://codeforces.com/gym/424075/problem/D
#Q: D. Find K

# Time: O(N)
# Space: O(N)

from collections import Counter

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = "NO"
    
    counter = Counter(arr)

    for value in arr:
        curr = value - k
        if curr in counter:
            if curr == value:
                if counter[curr] > 1:
                    ans = "YES"
                    break
            else:
                ans = "YES"
                break
    
    print(ans)
    return
                
t = int(input())
while t:
    solve()
    t -= 1