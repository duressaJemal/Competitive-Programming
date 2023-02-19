t = int(input())

for _ in range(t):

    a, b = map(int, input().split())
    modulo = a % b

    if modulo:
        print(b - modulo)
    else:
        print(modulo)