n, k = map(int, input().split())

odd_elements = n // 2 +  n % 2

if k <= odd_elements:
    print(k + (k - 1))
else:
    even_position = k - odd_elements
    print(even_position * 2)
