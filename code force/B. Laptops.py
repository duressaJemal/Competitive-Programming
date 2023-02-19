n = int(input())

combined = []
for _ in range(n):
    price, quality = map(int, input().split())
    combined.append((price, quality))

combined.sort()
is_valid = False

for index in range(1, n):
    if combined[index][1] < combined[index - 1][1]:
        is_valid = True
        break

if is_valid and n > 1:
    print("Happy Alex")
else:
    print("Poor Alex")
