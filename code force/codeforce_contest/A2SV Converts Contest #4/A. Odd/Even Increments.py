t = int(input())

for index in range(t):
    is_possible = True
    n = int(input())
    arr = list(map(int, input().split()))

    odd_index = "even" if arr[0] % 2 == 0 else "odd"
    even_index = "even" if arr[1] % 2 == 0 else "odd"

    for i in range(0, n, 2):
        value = "even" if arr[i] % 2 == 0 else "odd"
        if value != odd_index:
            is_possible = False
            break

    if is_possible:
        for i in range(1, n, 2):
            value = "even" if arr[i] % 2 == 0 else "odd"
            if value != even_index:
                is_possible = False
                break

    print("YES" if is_possible else "NO")