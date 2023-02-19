k, n, w = map(int, input().split())

value = (w * (w + 1)//2 * k) - n

print(value if value > 0 else 0)