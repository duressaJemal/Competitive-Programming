n = int(input())
arr = list(map(int, input().split()))

odd = False
even = False

for value in arr:
    if value % 2 == 0:
        even = True
    else:
        odd = True
    
    if odd and even:
        break

if odd and even:
    arr.sort()

print(*arr)