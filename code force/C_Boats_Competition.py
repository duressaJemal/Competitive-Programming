from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    max_count = 0
    counter = Counter(arr)

    for s in range(2, (2 * n) +  1):
        count = 0

        for i in range(1, (s + 1)//2):
            if s - i > n: continue
            count += min(counter[i], counter[s - i])
        
        if s % 2 == 0:
            count += counter[s//2]//2
        
        max_count = max(max_count, count)
    

    print(max_count)
    return
             
t = int(input())
while t:
    solve()
    t -= 1