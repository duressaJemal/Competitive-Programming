from collections import Counter


def solve():
    n, k = map(int, input().split())
    counter = Counter(input())
    result = 0

    ofset = ord("a")

    for i in range(26):

        lower = counter[chr(ofset + i)]
        upper = counter[chr(ofset + i - 32)]
        
        result += min(lower, upper)
        diff = abs(lower - upper) // 2

        if k >= diff:
            result += diff
            k -= diff
        else:
            if k:
                result += k
                k = 0

    print(result)

t = int(input())
while t:
    solve()
    t -= 1