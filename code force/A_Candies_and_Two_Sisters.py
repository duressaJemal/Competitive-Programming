from math import ceil


t = int(input())

for _ in range(t):

    n  = int(input())

    print(int(ceil(n / 2) - 1))