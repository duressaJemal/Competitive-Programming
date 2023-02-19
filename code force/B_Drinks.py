n = int(input())
p = list(map(int, input().split()))

amount = 0
for val in p:
    amount += val / 100

print(amount / n * 100)
