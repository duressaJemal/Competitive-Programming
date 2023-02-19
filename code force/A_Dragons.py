s, n = map(int, input().split())
combined = []

while n:
    current = tuple(map(int, input().split()))
    combined.append(current)
    n -= 1
combined.sort()

is_valid = True

for strength, bonous in combined:
    if s <= strength:
        is_valid = False
        break
    else:
        s += bonous
    
print("YES" if is_valid else "NO")
