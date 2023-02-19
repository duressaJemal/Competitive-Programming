from collections import defaultdict
from heapq import *


t = int(input())

while t:

    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))

    combined = []
    for index in range(n):
        combined.append((p[index], h[index]))
    combined.sort()

    total_damage = 0
    attack_power = k

    index = 0
    while attack_power > 0 and index < n:
        total_damage += attack_power
        if total_damage >= combined[index][1]:
            index += 1
        else:
            attack_power -= combined[index][0]
    
    if attack_power:
        print("YES")
    else:
        print("NO")

    t -= 1