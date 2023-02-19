t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(input())
    b = list(input())

    a.sort()
    b.sort()

    output = []
    count_a, count_b = 0, 0

    i, j = 0, 0
    while i < n and j < m:

        if (a[i] <= b[j] and count_a < k) or count_b == k:
            output.append(a[i])
            i += 1
            count_a += 1
            count_b = 0
        else:
            output.append(b[j])
            j += 1
            count_a = 0
            count_b += 1
        
    print("".join(output))


