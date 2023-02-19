n = int(input())
steps = 0
if n > 5:
    steps += n // 5
    n %= 5

if n:
    steps += 1

print(steps)