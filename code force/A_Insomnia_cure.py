k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

output = 0
for num in range(1, d + 1):
    hits = [k, l, m, n]
    for hit in hits:
        if num % hit == 0:
            output += 1
            break

print(output)