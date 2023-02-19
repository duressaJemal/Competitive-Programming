t = int(input())

for _ in range(t):

    n = int(input())

    for k in range(2, 32):
        x = n / (-1 + 2 ** k)

        if x > 0 and int(x) == x:
            print(int(x))
            break
    
